"""
Fuji TV programs retrieving

© Anime no Sekai — 2021
"""

import json
import pathlib
from datetime import datetime

from bs4 import BeautifulSoup
from pytz import timezone
from siesta.sdk.importer import absolute_import

correct_hour = absolute_import(pathlib.Path(__file__).parent.parent / "utils/time.py").correct_hour

# from ..utils.time import correct_hour
from siesta.sdk.providers.models import Bangumi
from siesta.server.utils.request import Session, SharedSession

JST = timezone("Asia/Tokyo")


def retrieve(session: Session = SharedSession):
    # https://www.fujitv.co.jp/bangumi/json/timetable_20210220.js
    try:
        current = datetime.now(JST).strftime("%Y%m%d")
        r = session.get(
            "https://www.fujitv.co.jp/bangumi/json/timetable_" +
            current +
            ".js")
        r.raise_for_status()
        data = json.loads(r.content)["contents"]["item"]
        results = []
        for program in data:
            try:
                _title = program.get("title", None)
                if _title is None:
                    _title = program.get("overview", "N/A")

                _start_date = program["start"].split("W")[0]
                _start_time = _start_date.split("T")[1]
                _start_hour = correct_hour(_start_time.split(":")[0])
                _start_other = ":".join(_start_time.split(":")[1:])
                start_date = _start_date.split(
                    "T")[0] + "T" + _start_hour + ":" + _start_other
                start_date = JST.localize(
                    datetime.fromisoformat(start_date))

                _end_date = program["end"].split("W")[0]
                _end_time = _end_date.split("T")[1]
                _end_hour = correct_hour(_end_time.split(":")[0])
                _end_other = ":".join(_end_time.split(":")[1:])
                end_date = _end_date.split(
                    "T")[0] + "T" + _end_hour + ":" + _end_other
                end_date = JST.localize(
                    datetime.fromisoformat(end_date))

                url = program.get("url", None)
                image = str(program.get("thumbnailGenreURL", ""))
                if image.replace(" ", "") == "":
                    image = str(program.get("logo", ""))

                results.append(Bangumi(
                    title=_title,
                    start=start_date.timestamp(),
                    end=end_date.timestamp(),
                    description=program.get("intro", "No description"),
                    url=url,
                    image=image
                ))
            except Exception:
                pass
        return results
    except Exception:
        return []
