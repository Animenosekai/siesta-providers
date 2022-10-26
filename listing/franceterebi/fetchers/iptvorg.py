from typing import Any

from ..data import iptvorg
from siesta.server.utils.request import Session, SharedSession


def fetch(session: Session = SharedSession) -> dict[str, list[tuple[str, Any]]]:
    output = {}
    for stream in ("fr", "fr_euronews", "fr_rakuten", "fr_samsung"):
        try:
            data = session.get("https://raw.githubusercontent.com/iptv-org/iptv/master/streams/{}.m3u".format(stream))
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
                        if tvg_id == "":
                            _, _, tvg_id = line.partition(",")
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
        except Exception:
            continue

    print(output)
    return output
