import json
import pathlib
from datetime import datetime, timedelta

from pytz import timezone
from siesta.sdk.importer import absolute_import
from siesta.sdk.providers.models import Bangumi
from siesta.server.utils.request import Session, SharedSession

mcas = absolute_import(pathlib.Path(__file__).parent / "mcas.py")
correct_hour = absolute_import(pathlib.Path(__file__).parent.parent / "utils/time.py").correct_hour
# from ..utils.time import correct_hour

JST = timezone("Asia/Tokyo")


def retrieve(session: Session = SharedSession):
    """
    Returns the list of today's programs on Tokyo MX (1)
    """
    # https://s.mxtv.jp/bangumi_file/json01/SV1EPG20210214.json
    try:
        current = datetime.now(JST).strftime("%Y%m%d")
        r = session.get(
            "https://s.mxtv.jp/bangumi_file/json01/SV1EPG" +
            current +
            ".json")
        r.raise_for_status()
        data = json.loads(r.content)
        results = []
        for program in data:
            try:
                _start_year, other = program["Start_time"].split("年")
                _start_month, other = other.split("月")
                _start_day, other = other.split("日")
                _start_hour, other = other.split("時")
                _start_minute, other = other.split("分")
                _start_second = other.split("秒")[0]
                start_date = JST.localize(
                    datetime(
                        year=int(_start_year),
                        month=int(_start_month),
                        day=int(_start_day),
                        hour=correct_hour(
                            int(_start_hour)),
                        minute=int(_start_minute),
                        second=int(_start_second)))

                _duration_hour, _duration_minute, _duration_second = program["Duration"].split(
                    ":")
                end_date = start_date + timedelta(
                    hours=int(_duration_hour),
                    minutes=int(_duration_minute),
                    seconds=int(_duration_second))

                _event_text = program.get("Event_text", "")
                _event_details = program.get("Event_details", "")
                if _event_text != "" and _event_details != "":
                    description = _event_text + "\n" + _event_details
                elif _event_text != "":
                    description = _event_text
                elif _event_details != "":
                    description = _event_details
                else:
                    description = None

                results.append(Bangumi(
                    title=program.get("Event_name", "N/A"),
                    start=start_date.timestamp(),
                    end=end_date.timestamp(),
                    description=description
                ))
            except Exception:
                pass
        return results
    except Exception:
        return mcas.retrieve(1, session=session)
