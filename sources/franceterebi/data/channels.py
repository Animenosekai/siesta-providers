from siesta.sdk.providers import tv_genres as genres

ALPEDHUEZ = "alpedhuez"
ANTENNE_REUNION = "antennereunion"
ARTE = "arte"
C8 = "c8"
CANALPLUS = "canalplus"
CHERIE_25 = "cherie25"
CNEWS = "cnews"
CSTAR = "cstar"
EURONEWS = "euronews"
FRANCE2 = "france2"
FRANCE3 = "france3"
FRANCE5 = "france5"
FRANCE24 = "france24"
FRANCEINFO = "franceinfo"
FRANCEINTER = "franceinter"
KTO = "kto"
LEQUIPE = "lequipe"
M6 = "m6"
MEZZO = "mezzo"
NRJ12 = "nrj12"
PUBLICSENAT = "publicsenat"
RMCDECOUVERTE = "rmcdecouverte"
TF1 = "tf1"
TF1SERIESFILMS = "tf1seriesfilms"
TFX = "tfx"
TMC = "tmc"
TV5MONDE = "tv5monde"
W9 = "w9"
RAKUTEN_ADN = "rakuten_adn"
RAKUTEN_FILMSACTION = "rakuten_filmsaction"
RAKUTEN_COMEDIES = "rakuten_comedies"
RAKUTEN_DRAMA = "rakuten_drama"
RAKUTEN_TOPFILMS = "rakuten_topfilms"
RAKUTEN_DOCUMENTARIES = "rakuten_documentaries"
RAKUTEN_FILMSFRANCAIS = "rakuten_filmsfrancais"
RAKUTEN_THRILLER = "rakuten_thrillers"
RAKUTEN_ROMANCE = "rakuten_romance"
RAKUTEN_FAMILY = "rakuten_family"
BFM_LILLE = "bfm_lille"
BFM_LITTORAL = "bfm_littoral"
VOSGESTV = "vosgestv"
VIAOCCITANIE = "viaoccitanie"

BFMTV = "bfmtv"
CANALPLUS_CINEMA = "canalplus_cinema"
CANALPLUS_SPORT = "canalplus_sport"
GULLI = "gulli"
LCI = "lci"
LCP = "lcp"
PARISPREMIERE = "parispremiere"
PLANETEPLUS = "planeteplus"
RMCSTORY = "rmcstory"
SIXTER = "sixter"  # 6ter


DATA = {
    ALPEDHUEZ: {
        "id": ALPEDHUEZ,
        "name": "Alpe d'Huez",
        "genre": genres.LOCAL
    },
    ANTENNE_REUNION: {
        "id": ANTENNE_REUNION,
        "name": "Antenne Réunion",
        "genre": genres.LOCAL
    },
    ARTE: {
        "id": ARTE,
        "name": "ARTE",
        "genre": genres.DOCUMENTARY
    },
    C8: {
        "id": C8,
        "name": "C8",
        "genre": genres.GENERAL
    },
    CANALPLUS: {
        "id": CANALPLUS,
        "name": "Canal Plus",
        "genre": genres.GENERAL
    },
    CHERIE_25: {
        "id": CHERIE_25,
        "name": "Chérie 25",
        "genre": genres.GENERAL
    },
    CNEWS: {
        "id": CNEWS,
        "name": "CNEWS",
        "genre": genres.NEWS
    },
    CSTAR: {
        "id": CSTAR,
        "name": "CSTAR",
        "genre": genres.ENTERTAINMENT
    },
    EURONEWS: {
        "id": EURONEWS,
        "name": "Euronews",
        "genre": genres.NEWS
    },
    FRANCE2: {
        "id": FRANCE2,
        "name": "France 2",
        "genre": genres.GENERAL
    },
    FRANCE3: {
        "id": FRANCE3,
        "name": "France 3",
        "genre": genres.GENERAL
    },
    FRANCE5: {
        "id": FRANCE5,
        "name": "France 5",
        "genre": genres.GENERAL
    },
    FRANCE24: {
        "id": FRANCE24,
        "name": "France 24",
        "genre": genres.NEWS
    },
    FRANCEINFO: {
        "id": FRANCEINFO,
        "name": "France Info",
        "genre": genres.NEWS
    },
    FRANCEINTER: {
        "id": FRANCEINTER,
        "name": "France Inter",
        "genre": genres.GENERAL
    },
    KTO: {
        "id": KTO,
        "name": "KTO TV",
        "genre": genres.RELIGIOUS
    },
    LEQUIPE: {
        "id": LEQUIPE,
        "name": "L'Equipe",
        "genre": genres.SPORTS
    },
    M6: {
        "id": M6,
        "name": "M6",
        "genre": genres.ENTERTAINMENT
    },
    MEZZO: {
        "id": MEZZO,
        "name": "Mezzo",
        "genre": genres.MUSIC
    },
    NRJ12: {
        "id": NRJ12,
        "name": "NRJ12",
        "genre": genres.ENTERTAINMENT
    },
    PUBLICSENAT: {
        "id": PUBLICSENAT,
        "name": "Public Sénat",
        "genre": genres.GENERAL
    },
    RMCDECOUVERTE: {
        "id": RMCDECOUVERTE,
        "name": "RMC Découverte",
        "genre": genres.DOCUMENTARY
    },
    TF1: {
        "id": TF1,
        "name": "TF1",
        "genre": genres.GENERAL
    },
    TF1SERIESFILMS: {
        "id": TF1SERIESFILMS,
        "name": "TF1 Séries/Films",
        "genre": genres.MOVIES
    },
    TFX: {
        "id": TFX,
        "name": "TFX",
        "genre": genres.ENTERTAINMENT
    },
    TMC: {
        "id": TMC,
        "name": "TMC",
        "genre": genres.ENTERTAINMENT
    },
    TV5MONDE: {
        "id": TV5MONDE,
        "name": "TV5MONDE",
        "genre": genres.NEWS
    },
    W9: {
        "id": W9,
        "name": "W9",
        "genre": genres.ENTERTAINMENT
    },
    RAKUTEN_ADN: {
        "id": RAKUTEN_ADN,
        "name": "Rakuten TV Anime Digital Network",
        "genre": genres.ANIMES
    },
    RAKUTEN_FILMSACTION: {
        "id": RAKUTEN_FILMSACTION,
        "name": "Rakuten TV Films Action",
        "genre": genres.MOVIES
    },
    RAKUTEN_COMEDIES: {
        "id": RAKUTEN_COMEDIES,
        "name": "Rakuten Comedy Movies France",
        "genre": genres.MOVIES
    },
    RAKUTEN_DRAMA: {
        "id": RAKUTEN_DRAMA,
        "name": "Rakuten TV Films Drames",
        "genre": genres.MOVIES
    },
    RAKUTEN_TOPFILMS: {
        "id": RAKUTEN_TOPFILMS,
        "name": "Rakuten TV Top Films",
        "genre": genres.MOVIES
    },
    RAKUTEN_DOCUMENTARIES: {
        "id": RAKUTEN_DOCUMENTARIES,
        "name": "Rakuten TV Documentaires",
        "genre": genres.DOCUMENTARY
    },
    RAKUTEN_FILMSFRANCAIS: {
        "id": RAKUTEN_FILMSFRANCAIS,
        "name": "Rakuten TV Films Français",
        "genre": genres.MOVIES
    },
    RAKUTEN_THRILLER: {
        "id": RAKUTEN_THRILLER,
        "name": "Rakuten TV Films Thriller",
        "genre": genres.MOVIES
    },
    RAKUTEN_ROMANCE: {
        "id": RAKUTEN_ROMANCE,
        "name": "Rakuten TV Romance",
        "genre": genres.MOVIES
    },
    RAKUTEN_FAMILY: {
        "id": RAKUTEN_FAMILY,
        "name": "Rakuten TV Famille",
        "genre": genres.MOVIES
    },
    BFM_LILLE: {
        "id": BFM_LILLE,
        "name": "BFM Grand Lille",
        "genre": genres.LOCAL
    },
    BFM_LITTORAL: {
        "id": BFM_LITTORAL,
        "name": "BFM Grand Littoral",
        "genre": genres.LOCAL
    },
    VOSGESTV: {
        "id": VOSGESTV,
        "name": "Vosges TV",
        "genre": genres.LOCAL
    },
    VIAOCCITANIE: {
        "id": VIAOCCITANIE,
        "name": "Via Occitanie",
        "genre": genres.LOCAL
    },
    BFMTV: {
        "id": BFMTV,
        "name": "BFMTV",
        "genre": genres.NEWS
    },
    CANALPLUS_CINEMA: {
        "id": CANALPLUS_CINEMA,
        "name": "Canal Plus Cinema",
        "genre": genres.MOVIES
    },
    CANALPLUS_SPORT: {
        "id": CANALPLUS_SPORT,
        "name": "Canal Plus Sport",
        "genre": genres.SPORTS
    },
    GULLI: {
        "id": GULLI,
        "name": "Gulli",
        "genre": genres.ENTERTAINMENT
    },
    LCI: {
        "id": LCI,
        "name": "LCI",
        "genre": genres.GENERAL
    },
    LCP: {
        "id": LCP,
        "name": "La Chaîne Parlementaire",
        "genre": genres.GENERAL
    },
    PARISPREMIERE: {
        "id": PARISPREMIERE,
        "name": "Paris Première",
        "genre": genres.MOVIES
    },
    PLANETEPLUS: {
        "id": PLANETEPLUS,
        "name": "Planète Plus",
        "genre": genres.MOVIES
    },
    RMCSTORY: {
        "id": RMCSTORY,
        "name": "RMC Story",
        "genre": genres.DOCUMENTARY
    },
    SIXTER: {
        "id": SIXTER,
        "name": "6ter",
        "genre": genres.DRAMAS
    }
}
