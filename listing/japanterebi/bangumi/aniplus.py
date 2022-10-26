"""
Aniplus programs retrieving

© Anime no Sekai — 2022
"""
from datetime import datetime, timedelta

from bs4 import BeautifulSoup
from pytz import timezone
from siesta.sdk.providers.models import Bangumi
from siesta.server.utils.request import Session, SharedSession

JST = timezone("Asia/Tokyo")


def retrieve(session: Session = SharedSession) -> list[Bangumi]:
    try:
        req = session.get("https://www.aniplus-asia.com/tv-schedule/")
        req.raise_for_status()
        page = BeautifulSoup(req.text, features="html.parser")
        results = []
        now = datetime.now(JST).replace(hour=0, minute=0, second=0, microsecond=0)  # the beginning of the day
        time = datetime.strptime(page.find("div", attrs={"class": "day1_schedule"}).text, "%A %b %d")
        time = time.replace(year=now.year - 1 if time.day > now.day and now.month == 1 else now.year)  # give the current year for now
        time = time + timedelta(hours=1)  # the first program on the schedule is in UTC+8, JST is UTC+9
        for tbody in page.find_all("tbody", attrs={"class": "wpsm-tbody"}):
            for tr in tbody.find_all("tr"):
                try:
                    infos = tr.find_all("td")
                    anchor = tr.find("a")
                    title = anchor.text
                    url = anchor["href"]

                    image = None
                    try:
                        soup = BeautifulSoup(session.get(url).text, "html.parser")
                        try:
                            image = soup.find("enlargestillcut")["src"]
                        except Exception:
                            pass
                        if image is None:
                            try:
                                image = soup.find("thumbstillcut")["src"]
                            except Exception:
                                pass
                            if image is None:
                                image = soup.find("meta", property="og:image")["content"]
                    except Exception:
                        pass

                    results.append(Bangumi(
                        title=title,
                        start=time.timestamp(),
                        end=(time + timedelta(minutes=30)).timestamp(),
                        genres=str(infos[5].text).split("/"),
                        description=f'"{infos[3].text}" | Episode {infos[2].text} for the anime「{title}」({infos[4].text})\nGenres: {infos[5].text}',
                        url=url,
                        image=image
                    ))
                except Exception:
                    continue
                time += timedelta(minutes=30)
        return results
    except Exception:
        return []
