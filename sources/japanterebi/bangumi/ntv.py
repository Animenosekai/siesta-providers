"""
NTV programs retrieving

© Anime no Sekai — 2021
"""

import pathlib

from siesta.sdk.importer import absolute_import

correct_hour = absolute_import(pathlib.Path(__file__).parent.parent / "utils/time.py").correct_hour
import json
from datetime import datetime

from pytz import timezone
from siesta.sdk.providers.models import Bangumi
from siesta.server.utils.request import Session, SharedSession

JST = timezone("Asia/Tokyo")


def retrieve(session: Session = SharedSession):
    """
    Returns the list of today's programs on NTV
    """
    # https://www.ntv.co.jp/program/json/program_list.json
    try:
        r = session.get("https://www.ntv.co.jp/program/json/program_list.json")
        r.raise_for_status()

        data = json.loads(r.content)
        results = []
        for program in data:
            try:
                _broadcast_date = program.get("broadcast_date")
                _year = int(_broadcast_date[:4])
                _month = int(_broadcast_date[4:6])
                _day = int(_broadcast_date[6:])

                _start_time = program.get("start_time")
                _start_hour = correct_hour(int(_start_time[:2]))
                _start_minute = int(_start_time[2:])

                _end_time = program.get("end_time")
                _end_hour = correct_hour(int(_end_time[:2]))
                _end_minute = int(_end_time[2:])

                _title = program.get("program_title_excluding_kakumi", None)
                if _title is None:
                    _title = program.get("program_title", None)
                    if _title is None:
                        _title = program.get("program_abbreviation", "N/A")

                _description = program.get("program_detail", None)
                if _description is None:
                    _description = program.get("program_content", None)

                image = None
                for img in program.get("image_names", []):
                    image = "https://www.ntv.co.jp/program/images/{}".format(img)
                    break

                results.append(Bangumi(
                    title=_title,
                    start=JST.localize(
                        datetime(
                            year=_year,
                            month=_month,
                            day=_day,
                            hour=_start_hour,
                            minute=_start_minute)).timestamp(),
                    end=JST.localize(
                        datetime(
                            year=_year,
                            month=_month,
                            day=_day,
                            hour=_end_hour,
                            minute=_end_minute)).timestamp(),
                    description=_description,
                    url=program.get("program_site_url", None),
                    image=image
                ))
            except Exception:
                pass
        return results
    except Exception:
        return []
