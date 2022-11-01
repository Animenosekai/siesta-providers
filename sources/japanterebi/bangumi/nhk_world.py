"""
NHK World programs retrieving

© Anime no Sekai — 2021
"""

import json
from datetime import datetime, timedelta

from pytz import timezone
from siesta.sdk.providers.models import Bangumi
from siesta.server.utils.request import Session, SharedSession

JST = timezone("Asia/Tokyo")


def retrieve(session: Session = SharedSession):
    # https://api.nhk.or.jp/nhkworld/epg/v7a/world/24h.json?apikey=EJfK8jdS57GqlupFgAfAAwr573q01y6k
    try:
        current = datetime.utcnow()
        start = current.replace(hour=0, minute=0, second=0, microsecond=0)
        end = current.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        r = session.get("https://nwapi.nhk.jp/nhkworld/epg/v7b/world/s{}-e{}.json".format(int(start.timestamp() * 1000), int(end.timestamp() * 1000)))
        r.raise_for_status()
        data = json.loads(r.content)["channel"]["item"]
        results = []
        for program in data:
            try:
                start_date = JST.localize(
                    datetime.fromtimestamp(int(program["pubDate"]) / 1000))
                end_date = JST.localize(
                    datetime.fromtimestamp(int(program["endDate"]) / 1000))

                _url = program.get("url", None)
                if _url is not None:
                    _url = "https://www3.nhk.or.jp{}".format(_url.replace("\\", ""))

                image = str(program.get("thumbnail", ""))
                if image.replace(" ", "") == "":
                    image = str(program.get("thumbnail_s", ""))
                if image.replace(" ", "") != "":
                    image = "https://www3.nhk.or.jp{}".format(image)

                results.append(Bangumi(
                    title=program.get("title", "N/A"),
                    start=start_date.timestamp(),
                    end=end_date.timestamp(),
                    description=program.get("description", None),
                    url=_url,
                    image=image
                ))
            except Exception:
                pass
        return results
    except Exception:
        return []
