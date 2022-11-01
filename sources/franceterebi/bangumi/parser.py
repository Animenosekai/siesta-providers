import json
from datetime import datetime
from pathlib import Path

from siesta.sdk.providers.models import Bangumi
from siesta.server.utils.request import Session, SharedSession


def parse_datetime(date: str):
    data = {
        "year": int(date[:4]),
        "month": int(date[4:6]),
        "day": int(date[6:8]),
        "hour": int(date[8:10]),
        "minute": int(date[10:12]),
        "second": int(date[12:])
    }

    return datetime(**data)


def retrieve(channel: str, session: Session = SharedSession):
    with Path(__file__).parent.parent / "data" / "bangumi.json" as f:
        data = json.loads(f.read_text())

    results = []
    for programme in data["tv"]["programme"]:
        if programme["@channel"] != channel:
            continue

        start, _, _ = str(programme["@start"]).partition(" ")
        start = parse_datetime(start).timestamp()

        end, _, _ = str(programme["@stop"]).partition(" ")
        end = parse_datetime(end).timestamp()

        if programme["rating"]["@system"] == "CSA":
            rating = str(programme["rating"]["value"]).lower().replace(" ", "")
            if rating.startswith("tout"):
                age = 0
            else:
                age = int(rating.removeprefix("-"))
        else:
            age = None

        results.append(Bangumi(
            title=programme["title"]["#text"],
            start=start,
            end=end,
            age=age,
            description=programme["desc"]["#text"],
            image=programme["icon"]["@src"],
        ))

    return results
