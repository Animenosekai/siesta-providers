from siesta.server.utils.request import Session, SharedSession
import pyuseragents


def fetch(session: Session = SharedSession):
    return {
        "tokyomx": [("https://movie.mcas.jp/mcas/mx1_2/chunklist.m3u8", {"User-Agent": pyuseragents.random()})],
        "tokyomx2": [("https://movie.mcas.jp/mcas/mx2_2/chunklist.m3u8", {"User-Agent": pyuseragents.random()})],
        "gunma": [("https://movie.mcas.jp/switcher/mcas8_2/chunklist.m3u8", {"User-Agent": pyuseragents.random()})],
        "weather_news": [("https://movie.mcas.jp/mcas/wn1_2/chunklist.m3u8", {"User-Agent": pyuseragents.random()})],
        "nhk_world": [("https://nhkworld.webcdn.stream.ne.jp/www11/nhkworld-tv/global/2003458/live.m3u8", {"User-Agent": pyuseragents.random()})],
        "ntv_news": [("https://www.news24.jp/livestream/index.m3u8", {"User-Agent": pyuseragents.random()})],
        "qvc": [("https://cdn-live1.qvc.jp/iPhone/1501/1501.m3u8", {"User-Agent": pyuseragents.random()})],
        "shopchannel": [("https://stream3.shopch.jp/HLS/master.m3u8", {"User-Agent": pyuseragents.random()})],
        "gakinotsukai": [("https://hamada.gaki-no-tsukai.eu:2087/hls/test.m3u8", {"User-Agent": pyuseragents.random()})],
        "animetv": [("https://stmv1.srvif.com/animetv/animetv/chunklist_w1754210614.m3u8", {"User-Agent": pyuseragents.random()})],
        "aniplus": [("http://45.126.83.51/dr9445/h/h02/01.m3u8", {"User-Agent": pyuseragents.random()})]
    }
