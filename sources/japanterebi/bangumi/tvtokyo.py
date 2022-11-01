import json
from datetime import datetime, timedelta

from pytz import timezone
from siesta.sdk.providers.models import Bangumi
from siesta.server.utils.request import Session, SharedSession

JST = timezone("Asia/Tokyo")


def retrieve(session: Session = SharedSession):
    """
    Returns the list of today's programs on TV Tokyo
    """
    # https://www.tv-tokyo.co.jp/tbcms/assets/data/20210214.json
    try:
        current = datetime.now(JST).strftime("%Y%m%d")
        r = session.get(
            "https://www.tv-tokyo.co.jp/tbcms/assets/data/" +
            current +
            ".json")
        r.raise_for_status()
        data = json.loads(r.content)
        results = []
        already_verified = []
        delta = timedelta(hours=6)
        for timing in data:
            try:
                timing = data[timing]
                if "1" in timing:
                    program_title = timing["1"].get("title", "N/A")
                    if program_title not in already_verified and program_title != False:
                        program = timing["1"]
                        start_date = JST.localize(
                            datetime.fromtimestamp(program["sts"] / 1000) + delta)
                        end_date = JST.localize(
                            datetime.fromtimestamp(program["ets"] / 1000) + delta)

                        _url = program.get("url", "")
                        if _url == False:
                            _url = ""
                        if _url.replace(" ", "") != "" and not _url.startswith("https:"):
                            _url = "https:{}".format(_url)

                        image_data = program.get("image", {})
                        image = str(image_data.get("file_path", "")).replace("\\", "")
                        if image.replace(" ", "") != "" and not image.startswith("https:"):
                            image = "https:{}".format(image)

                        results.append(Bangumi(
                            title=program_title,
                            start=start_date.timestamp(),
                            end=end_date.timestamp(),
                            description=program.get(
                                "description", None),
                            url=_url,
                            image=image
                        ))
                        already_verified.append(program_title)
            except Exception:
                pass
        return results
    except Exception:
        return []
