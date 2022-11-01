"""
TV Asahi programs retrieving

© Anime no Sekai — 2021
"""

import json
from datetime import datetime

from pytz import timezone
from siesta.sdk.providers.models import Bangumi
from siesta.server.utils.request import Session, SharedSession

JST = timezone("Asia/Tokyo")


def retrieve(session: Session = SharedSession):
    """
    Returns the list of today's programs on TV Asahi
    """
    # https://www.tv-asahi.co.jp/common/json/NowOnair/3days.json
    try:
        r = session.get("https://www.tv-asahi.co.jp/common/json/NowOnair/3days.json")
        r.raise_for_status()
        data = json.loads(r.content)
        results = []
        for program in data:
            try:
                _date_year, _date_month, _date_day = int(
                    program
                    ["OnAirDate"]
                    [: 4]), int(
                    program["OnAirDate"][4: 6]), int(
                    program["OnAirDate"][6:])
                _start_hour, _start_minute = int(
                    program["StartTime"][: 2]), int(
                    program["StartTime"][2:])
                start_date = JST.localize(
                    datetime(
                        year=_date_year,
                        month=_date_month,
                        day=_date_day,
                        hour=_start_hour,
                        minute=_start_minute))

                _end_hour, _end_minute = int(
                    program["EndTime"][:2]), int(program["EndTime"][2:])
                end_date = JST.localize(
                    datetime(
                        year=_date_year,
                        month=_date_month,
                        day=_date_day,
                        hour=_end_hour,
                        minute=_end_minute))

                _url = str(program.get("PcUrl", ""))
                if _url == "":
                    _url = None
                else:
                    _url = str(_url).replace("\\", "")

                image = str(program.get("ImageUrl", ""))
                if image == "":
                    image = None
                else:
                    image = str(image).replace("\\", "")

                results.append(Bangumi(
                    title=str(program["ProgramName"]),
                    start=start_date.timestamp(),
                    end=end_date.timestamp(),
                    url=_url,
                    image=image
                ))
            except Exception:
                pass
        return results
    except Exception:
        return []
