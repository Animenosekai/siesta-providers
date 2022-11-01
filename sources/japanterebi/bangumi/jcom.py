import json
from datetime import datetime

from bs4 import BeautifulSoup
from pytz import timezone
from rich.console import Console
from siesta.sdk.providers.models import Bangumi
from siesta.server.utils.request import Session, SharedSession

console = Console()

JST = timezone("Asia/Tokyo")


def retrieve(service_code: str, location: int = 2, session: Session = SharedSession) -> list[Bangumi]:
    try:
        current = datetime.now(JST).strftime("%Y%m%d")
        channel = "{}_{}_{}".format(location, service_code, current)
        r = session.get(
            "https://tvguide.myjcom.jp/api/getEpgInfo/?channels=" +
            channel +
            "&rectime=&rec4k=")
        r.raise_for_status()
        data = json.loads(r.content)[channel]
        results = []
        for program in data:
            try:
                _start_date = str(program["programStart"])
                _start_year, _start_month, _start_day, _start_hour, _start_minute, _start_second = int(_start_date[:4]), int(
                    _start_date[4:6]), int(_start_date[6:8]), int(_start_date[8:10]), int(_start_date[10:12]), int(_start_date[12:]),
                start_date = JST.localize(
                    datetime(
                        year=_start_year,
                        month=_start_month,
                        day=_start_day,
                        hour=_start_hour,
                        minute=_start_minute,
                        second=_start_second))
                _end_date = str(program["programEnd"])
                _end_year, _end_month, _end_day, _end_hour, _end_minute, _end_second = int(_end_date[:4]), int(
                    _end_date[4:6]), int(_end_date[6:8]), int(_end_date[8:10]), int(_end_date[10:12]), int(_end_date[12:]),
                end_date = JST.localize(
                    datetime(
                        year=_end_year,
                        month=_end_month,
                        day=_end_day,
                        hour=_end_hour,
                        minute=_end_minute,
                        second=_end_second))
                if "eventId" in program and "programDate" in program:
                    _url = "https://tvguide.myjcom.jp/detail/?channelType=120&serviceCode=182_65406&eventId=" + \
                        str(program["eventId"]) + "&programDate=" + str(program["programDate"])
                else:
                    _url = None

                image = program.get("imgPath", None)
                if image is not None:
                    image = "https://tvguide.myjcom.jp{}".format(str(image).replace("\\", ""))

                results.append(Bangumi(
                    title=program["title"],
                    start=start_date.timestamp(),
                    end=end_date.timestamp(),
                    description=program.get("commentary", None),
                    url=_url,
                    image=image
                ))
            except Exception:
                pass
        return results
    except Exception:
        return []
