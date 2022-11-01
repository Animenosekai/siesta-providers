import json
from datetime import datetime

from pytz import timezone
from siesta.sdk.providers.models import Bangumi
from siesta.server.utils.request import Session, SharedSession

JST = timezone("Asia/Tokyo")


def retrieve(channel: int, session: Session = SharedSession):
    """
    Returns the list of today's programs on Tokyo MX, Tokyo MX 2, Weather News and Gunma
    """
    # https://mcas.jp/api/v3/airtimes/2days/20210215
    try:
        current = datetime.now(JST).strftime("%Y%m%d")
        r = session.get("https://mcas.jp/api/v3/airtimes/2days/" + current)
        r.raise_for_status()
        data = json.loads(r.content)["data"]
        results = []
        for program in data:
            if program["channel_id"] != channel:
                continue

            metadata = program["program"]

            _description = metadata.get("description", None)
            if _description is None:
                _description = metadata.get("program_description", None)

            _url = metadata.get("url", None)

            results.append(Bangumi(
                title=metadata.get("name", "N/A"),
                start=datetime.fromisoformat(program["started_at"]).timestamp(),
                end=datetime.fromisoformat(program["finished_at"]).timestamp(),
                description=_description,
                url=_url
            ))
        return results
    except Exception:
        return []
