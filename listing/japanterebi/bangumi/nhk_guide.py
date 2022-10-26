import json
from datetime import datetime

from pytz import timezone
from siesta.sdk.providers.models import Bangumi
from siesta.server.utils.request import Session, SharedSession

JST = timezone("Asia/Tokyo")


def retrieve(channel: str, session: Session = SharedSession) -> list[Bangumi]:
    """
    Returns the list of today's programs on NHK General
    """
    # https://api.nhk.or.jp/r5/pg/list/4/130/all/2021-02-14.json
    # --> Here are the constants: https://api.nhk.jp/r6/const.json?ignoreRange=true
    # --> the params preceding the date are explained in the API docs
    try:
        current = datetime.now(JST).strftime("%Y-%m-%d")
        r = session.get(
            "https://api.nhk.or.jp/r5/pg/list/4/130/all/" +
            current +
            ".json")
        r.raise_for_status()
        data = json.loads(r.content)["list"][channel]
        results = []
        for program in data:
            try:
                _description = program.get("content", None)
                if _description is None:
                    _description = program.get("subtitle", None)

                url_data = program.get("url", {})
                url = url_data.get("pc", "")
                if url.replace(" ", "") == "":
                    url = url_data.get("i", "")
                if url.replace(" ", "") == "":
                    url = url_data.get("e", "")
                if url.replace(" ", "") == "":
                    url = url_data.get("v", "")
                if url.replace(" ", "") == "":
                    url = url_data.get("short", "")

                images_data = program.get("images", {})
                image = str(images_data.get("posterframe_m", {}).get("url", ""))
                if image.replace(" ", "") == "":
                    image = str(images_data.get("thumbnail_m", {}).get("url", ""))
                if image.replace(" ", "") == "":
                    image = str(images_data.get("logo_l", {}).get("url", ""))

                if image.replace(" ", "") == "":
                    pr_data = program.get("extra", {}).get("pr_images", [])
                    for d in pr_data:
                        image = d.get("keyvisual_ll", {}).get("url", "")
                        if image.replace(" ", "") == "":
                            image = d.get("keyvisual_l", {}).get("url", "")
                        if image.replace(" ", "") == "":
                            image = d.get("keyvisual_s", {}).get("url", "")
                        
                        if image.replace(" ", "") != "":
                            break
                
                results.append(Bangumi(
                    id=program.get("id", None),
                    title=program.get("title", "N/A"),
                    start=datetime.fromisoformat(
                        program["start_time"]).timestamp(),
                    end=datetime.fromisoformat(program["end_time"]).timestamp(),
                    description=_description,
                    url=url,
                    image=image
                ))
            except Exception:
                pass
        return results
    except Exception:
        return []
