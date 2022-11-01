import datetime
import itertools
from base64 import b64encode
from math import exp, log
from multiprocessing.pool import ThreadPool
from pathlib import Path
from typing import Literal, Union

import m3u8
import pyuseragents
from rich.console import Console
from siesta.sdk.encoder.ffmpeg import FFmpeg
from siesta.sdk.encoder.presets import Encoder, Profile
from siesta.sdk.encoder.probe import Probe
from siesta.sdk.providers import tv_genres as genres
from siesta.sdk.providers.models import (Bangumi, Channel, Fragment, Provider,
                                         Source, BaseTVProvider)
from siesta.server.db import SiestaDB
from siesta.server.utils.request import Session, SharedSession
from yuno.security.encrypt import AES
from yuno.security.hash import Hasher
from yuno.security.token import TokenManager

from . import bangumi, fetchers
from .data import channels

console = Console()
hasher = Hasher()
aes = AES(SiestaDB.siesta, prefix="japanterebi")
token_manager = TokenManager(key=SiestaDB.siesta)


class Playlist:
    DIMENSION_WEIGHT = 0.4
    FPS_WEIGHT = 0.3
    TIME_WEIGHT = 0.2
    BITRATE_WEIGHT = 0.2

    def __init__(self, url: str, content: m3u8.M3U8, master_playlist: m3u8.Playlist = None, headers: dict = None, session: Session = None) -> None:
        self.url = str(url)
        # self.id = hasher.hash_string(self.url)

        self.session = session or SharedSession

        self.headers = headers or {}
        if "User-Agent" not in self.headers:
            self.headers["User-Agent"] = pyuseragents.random()

        self.content = content

        request = self.session.get(self.content.segments[0].absolute_uri, headers=self.headers)
        self.time = request.elapsed.total_seconds()
        self.first_fragment = request.content

        self.probe = Probe(self.first_fragment)
        self.bitrate = self.probe.bit_rate
        self.width = self.probe.video.width
        self.height = self.probe.video.height
        self.fps = self.probe.video.fps
        self.video_codec = None
        self.audio_codec = None

        if master_playlist is not None:
            si = master_playlist.stream_info
            self.video_codec, self.audio_codec = str(si.codecs).split(",")[:2]
            if not self.bitrate and si.bandwidth:
                self.bitrate = int(si.bandwidth)
            if not self.bitrate and si.average_bandwidth:
                self.bitrate = int(si.average_bandwidth)
            if not self.height or not self.width and si.resolution:
                self.width, self.height = [int(r) for r in str(si.resolution).split("x")]
            if not self.fps and si.frame_rate:
                self.fps = int(si.frame_rate)

        if self.video_codec is None:
            self.video_codec = self.probe.video.codec
        if self.audio_codec is None:
            self.audio_codec = self.probe.audio.codec

    @property
    def score(self) -> float:
        """
        Computing the fragment score, based on the first fragment in the playlist
        """
        height = -1.45 * exp((-1 * 15 / 10_000) * self.height) + 1
        width = -1.45 * exp((-1 * 9 / 10_000) * self.width) + 1
        if self.fps:
            try:
                fps = 0.3 * log(6 * self.fps - 75) - 0.89
            except Exception:
                fps = 0
        else:
            fps = 0
        if self.bitrate:
            bitrate = (-1 / 10_000_000) * (((self.bitrate / 1000) - 4000) ** 2) + 1  # in kbit/s
        else:
            bitrate = 0
        time = 1.5 ** (-1 * self.time)
        return (
            (height + width) * (self.DIMENSION_WEIGHT / 2)
            + fps * self.FPS_WEIGHT
            + time * self.TIME_WEIGHT
            + bitrate * self.BITRATE_WEIGHT
        )

    def as_dict(self) -> dict:
        return {
            "url": self.url,
            "headers": self.headers,
            "bitrate": self.bitrate,
            "height": self.height,
            "width": self.width,
            "fps": self.fps,
            "videoCodec": self.video_codec,
            "audioCodec": self.audio_codec,
            "time": self.time,
            "score": self.score
        }

    def __repr__(self) -> str:
        return 'Playlist("{}")'.format(self.url)


class JapanTerebi(Provider):
    NAME = "Japan Terebi"
    VERSION = (1, 0, 0)
    DESCRIPTION: str = "Watch your favorite japanese shows in realtime!"

    def __init__(self) -> None:
        """
        Japan Terebi provides multiple Japanese TV Channels, gathering them from different sources.
        """
        super().__init__()

    def on_update(self):
        try:
            data = fetchers.fetch(self.session)

            results = {}
            with ThreadPool(10) as main_pool:
                def _process(channel, links):
                    results = {}
                    with ThreadPool(5) as tpool:
                        def _retrieve(link):
                            link, headers = link if isinstance(link, tuple) else (link, None)
                            return self.tv.get_playlists(link, headers=headers)
                        channel_playlists: list[Playlist] = list(itertools.chain.from_iterable(tpool.map(func=_retrieve, iterable=links)))

                    if len(channel_playlists) <= 0:
                        return []
                    channel_playlists = sorted(channel_playlists, key=lambda x: x.score, reverse=True)

                    self.tv.thumbnails_path.mkdir(parents=True, exist_ok=True)

                    try:
                        FFmpeg(
                            channel_playlists[0].first_fragment,
                            vf="thumbnail,scale=-2:240",
                            vframes=1
                        ).run(self.tv.thumbnails_path / "{}.jpg".format(channel))
                    except Exception:
                        console.print_exception()

                    for playlist in channel_playlists:
                        try:
                            results[channel].append(playlist.as_dict())
                        except KeyError:
                            results[channel] = [playlist.as_dict()]

                    return results

                for r in main_pool.starmap(func=_process, iterable=data.items()):
                    results.update(r)

            channels_before = [d["_id"] for d in self.db.find(include=["_id"])]

            for channel, links in results.items():
                channel = str(channel)
                self.db[channel] = {
                    "sources": links,
                    "bangumi": [b.as_dict() for b in bangumi.Bangumis[channel].retrieve(self.session)] if channel in bangumi.Bangumis else []
                }
        except Exception:
            from rich.console import Console
            Console().print_exception()
            raise

        for channel in set(channels_before).difference(set(results.keys())):
            del self.db[channel]

    class TVProvider(BaseTVProvider):
        def __init__(self, parent) -> None:
            super().__init__(parent)
            self.thumbnails_path = Path(__file__).parent / "thumbnails"
            self.thumbnails_path.mkdir(parents=True, exist_ok=True)

        def get_playlists(self, url: str, headers: dict = None, master_playlist: m3u8.Playlist = None) -> list[Playlist]:
            """
            Recursively retrieves all of the segments playlists
            """
            results = []
            try:
                request = self.session.get(url, headers=headers)
                content = m3u8.loads(request.text, uri=url)

                if len(content.segments) > 0:
                    try:
                        results.append(Playlist(url, content, master_playlist=master_playlist, headers=headers, session=self.session))
                    except Exception:
                        # console.print_exception()
                        pass

                for playlist in content.playlists:
                    results.extend(self.get_playlists(playlist.absolute_uri, headers=headers, master_playlist=playlist))

            except Exception:
                # console.print_exception()
                pass
            return results

        def get_channels(self) -> list[Channel]:
            found = self.db.find(include=["_id"])
            results = []
            for channel in found:
                channel_id = channel["_id"]
                logo_path = Path("server/providers/japanterebi/data/logo/{}.png".format(channel_id))
                try:
                    logo_data = logo_path.read_bytes()
                    logo_data = "data:image/png;base64,{}".format(b64encode(logo_data).decode("utf-8"))
                except Exception:
                    logo_data = None
                results.append(Channel(
                    id=channel_id,
                    name=channels.DATA[channel_id]["name"],
                    description=channels.DATA[channel_id].get("description", "There is no description for this channel"),
                    genre=channels.DATA[channel_id].get("genre", genres.OTHER),
                    country="Japan",
                    logo=logo_data
                ))
            return results

        def get_channel(self, channel: str) -> Channel:
            if channel not in channels.DATA:
                return super().get_channel(channel)

            logo_path = Path("server/providers/japanterebi/data/logo/{}.png".format(channel))
            try:
                logo_data = logo_path.read_bytes()
                logo_data = "data:image/png;base64,{}".format(b64encode(logo_data).decode("utf-8"))
            except Exception:
                logo_data = None
            return Channel(
                id=channel,
                name=channels.DATA[channel]["name"],
                description=channels.DATA[channel].get("description", "There is no description for this channel"),
                genre=channels.DATA[channel].get("genre", genres.OTHER),
                country="Japan",
                logo=logo_data
            )

        def get_channel_original_source(self, channel: str) -> list[Source]:
            found = self.db.find(_id=str(channel), include=["sources"])[0]
            results = []
            for source in found["sources"]:
                results.append(Source(
                    id=token_manager.generate(extra={
                        "url": source["url"],
                        "headers": source["headers"]
                    }, encryption=aes, expire=datetime.timedelta(days=7)),
                    bitrate=source["bitrate"],
                    video_codec=source["videoCodec"],
                    audio_codec=source["audioCodec"],
                    width=source["width"],
                    height=source["height"],
                    fps=source.get("fps", None)
                ))
            return results

        def get_right_source(self, channel: str, profile: tuple[Literal["original", "transcoded"], Union[Profile, str]] = None):
            type, level = profile
            if type == "original":
                data = token_manager.decode(level, encryption=aes)["data"]
                return data
            found = self.db.find(_id=str(channel), include=["sources"])[0]
            sources = sorted(found["sources"], key=lambda x: x["height"])
            for source in sources:
                if source["height"] >= level.height:
                    return source
            return sources[-1]

        def get_channel_fragments(self, channel: str, profile: tuple[Literal["original", "transcoded"], Union[Profile, str]] = None) -> list[Fragment]:
            source = self.get_right_source(channel, profile)
            request = self.session.get(source["url"], headers=source["headers"])
            playlist = m3u8.loads(request.text, uri=source["url"])
            return playlist.media_sequence, [Fragment(
                name=token_manager.generate(encryption=aes, frag=frag.absolute_uri, headers=source["headers"]),
                duration=datetime.timedelta(seconds=float(frag.duration))
            ) for frag in playlist.segments]

        def get_channel_fragment(self, channel: str, fragment: str, profile: tuple[Literal["original", "transcoded"], Union[Profile, str]] = None, encoder: Encoder = ...) -> bytes:
            data = token_manager.decode(fragment, encryption=aes)["data"]
            request = self.session.get(data["frag"], headers=data["headers"])
            return request.content

        def get_channel_thumbnail(self, channel: str) -> bytes:
            path = self.thumbnails_path / "{}.jpg".format(channel)
            return path.read_bytes()

        def get_channel_bangumi(self, channel: str) -> list[Bangumi]:
            found = self.db.find(_id=str(channel), include=["bangumi"])[0]
            return [Bangumi(**b) for b in found["bangumi"]]
