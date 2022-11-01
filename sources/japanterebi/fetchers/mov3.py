from bs4 import BeautifulSoup
from siesta.server.utils.request import Session, SharedSession
from youtube_dl import YoutubeDL
from yt_dlp import YoutubeDL as YoutubeDLP

AVAILABLE_CHANNELS = [
    "ntv",
    "fujitv",
    "tbs",
    "nhk",
    "tvtokyo",
    "tokyomx"
]


def fetch_channel(channel: str, session: Session = SharedSession):
    embed = None
    r = session.get("http://mov3.co/embed{}.html".format(channel))
    if r.status_code < 400:
        soup = BeautifulSoup(r.text, "html.parser")
        try:
            embed = soup.find("script").text
        except Exception:
            pass

    if embed:
        _, _, content = embed.partition("file" if "jwplayer" in embed else "src")
        result = ""
        preparing = False
        parsing = False
        for char in content:
            if char == ":":
                preparing = True
            if char == '"' and preparing:
                parsing = True
            if char == '"' and parsing:
                break
            if parsing:
                result += char
        return result, None

    r = session.get("http://mov3.co/{}".format(channel))
    r.raise_for_status()
    page = r.text
    soup = BeautifulSoup(page, "html.parser")
    link = None

    for iframe in soup.find_all("iframe"):
        if "ok.ru" in iframe["src"]:
            link = iframe["src"]

    if link is None:
        raise ValueError("'link' cannot be None")

    link = str(link)
    if not link.startswith("https:"):
        link = "https:{}".format(link)

    try:
        with YoutubeDL({"format": "best"}) as ydl:
            results = ydl.extract_info(link, download=False)
            return results["url"], {"User-Agent": results["http_headers"]["User-Agent"]}
    except Exception:
        with YoutubeDLP({"format": "best"}) as ydl:
            results = ydl.extract_info(link, download=False)
            return results["url"], {"User-Agent": results["http_headers"]["User-Agent"]}


def fetch(session: Session = SharedSession):
    results = {}
    for channel in AVAILABLE_CHANNELS:
        try:
            results[channel] = [fetch_channel(channel, session=session)]
        except Exception:
            continue
    return results
