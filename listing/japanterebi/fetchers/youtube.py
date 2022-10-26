import json

import pyuseragents

try:
    from .__youtube import API_KEY
except ImportError:
    API_KEY = None
from siesta.server.utils.request import Session, SharedSession
from youtube_dl import YoutubeDL
from yt_dlp import YoutubeDL as YoutubeDLP


def fetch(session: Session = SharedSession):
    try:
        if API_KEY is None:
            raise ValueError("There is no YouTube Data API Key")
        r = session.get(
            "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=UCGCZAYq5Xxojl_tSXcVJhiQ&q=JapaNews&type=video&key={}".format(API_KEY=API_KEY))
        r.raise_for_status()

        # JapaNews 24
        data = json.loads(r.content)["items"][0]
        link = "https://youtu.be/" + data["id"]["videoId"]

        try:
            data = YoutubeDL({"format": "best"}).extract_info(link, download=False)
        except Exception:
            data = YoutubeDLP({"format": "best"}).extract_info(link, download=False)

        if data["is_live"]:
            url = data.get("manifest_url", None)
            if url is None:
                url = data["url"]
            if url is not None:
                return {"japanews": [(url, {"User-Agent": pyuseragents.random()})]}
        return {}
    except Exception:
        return {}
