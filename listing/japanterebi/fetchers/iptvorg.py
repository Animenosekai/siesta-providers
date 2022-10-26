from typing import Any

from ..data import iptvorg
from siesta.server.utils.request import Session, SharedSession


def fetch(session: Session = SharedSession) -> dict[str, list[tuple[str, Any]]]:
    data = session.get("https://raw.githubusercontent.com/iptv-org/iptv/master/streams/jp.m3u")
    output = {}
    current_channel = ""
    for line in data.text.split("\n"):
        try:
            line = str(line).replace("\n", "")
            # parsing the m3u file
            if line.startswith("#EXTM3U"):
                continue
            if line.startswith("#EXTVLCOPT"):
                continue
            elif line.startswith("#EXTINF:-1"):
                tvg_id = line[19:].split('"')[0]
                try:
                    current_channel = iptvorg.ID_MAPPING[tvg_id]
                except Exception:
                    current_channel = ""
                    continue
            else:
                if current_channel == "" or line == "":
                    continue
                try:
                    output[current_channel].append(line)
                except KeyError:
                    output[current_channel] = [line]
        except Exception:
            continue
    return output
