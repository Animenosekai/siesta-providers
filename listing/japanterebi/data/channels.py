from siesta.sdk.providers import tv_genres as genres

NTV = "ntv"
FUJITV = "fujitv"
TBS = "tbs"
TOKYOMX = "tokyomx"
TOKYOMX2 = "tokyomx2"
NHK_WORLD = "nhk_world"
ANIMAX = "animax"
GUNMA = "gunma"
NTV_NEWS = "ntv_news"
WEATHER_NEWS = "weather_news"
NHK = "nhk"
TVASAHI = "tvasahi"
TVTOKYO = "tvtokyo"
ATX = "atx"
JAPANEWS = "japanews"
BSASAHI = "bsasahi"
BSFUJI = "bsfuji"
BSTVTOKYO = "bstvtokyo"
ETERE = "etere"
BSNHK = "bsnhk"
BSNHKPREMIUM = "bsnhkpremium"
BS11 = "bs11"
BSNTV = "bsntv"
BSTBS = "bstbs"
BSFUJITV = "bsfujitv"
BSNIPPONTV = "bsnippontv"
QVC = "qvc"
SHOPCHANNEL = "shopchannel"
GAKINOTSUKAI = "gakinotsukai"
JAPANET = "japanet"
HIROSHIMAHOME = "hiroshimahome"
ANIMETV = "animetv"
ANIPLUS = "aniplus"
# FAMILYGEKIJO = "familygekijo"
GAORA = "gaora"
JSPORTS1 = "jsports1"
JSPORTS2 = "jsports2"
JSPORTS3 = "jsports3"
JSPORTS4 = "jsports4"
KANSAITV = "kansaitv"
MAINICHIBS = "mainichibs"
TVOSAKA = "tvosaka"
WAKUWAKU = "wakuwaku"


DATA = {
    NTV: {
        "id": NTV,
        "name": "NTV",
        "description": "Nippon Television Network Corporation (日本テレビ放送網株式会社 Nippon Terebi Hōsōmō Kabushiki-gaisha), doing business as Nippon TV, is a television network based in the Shiodome area of Minato, Tokyo, Japan and is controlled by the Yomiuri Shimbun publishing company. Broadcasting terrestrially across Japan, the network is commonly known as Nihon Terebi (日本テレビ), contracted to Niitere (日テレ), and abbreviated as \"NTV\" or \"AX\".",
        "genre": genres.GENERAL
    },
    FUJITV: {
        "id": FUJITV,
        "name": "Fuji TV",
        "description": "Fuji Television Network, Inc. (株式会社フジテレビジョン, Kabushiki gaisha Fuji Terebijon) is a Japanese television station based in Odaiba, Minato, Tokyo, Japan, also known as Fuji TV (フジテレビ, Fuji Terebi) or CX, based on the station's call sign \"JOCX-DTV\". It is the flagship station of the Fuji News Network (FNN) and the Fuji Network System. It is also known for its long-time slogan, \"If it's not fun, it's not TV!\" Fuji Television also operates three premium television stations, known as \"Fuji TV One\" (\"Fuji TV 739\"—sports/variety), \"Fuji TV Two\" (\"Fuji TV 721\"—drama/anime), and \"Fuji TV Next\" (\"Fuji TV CSHD\"—live premium shows) (called together as \"Fuji TV OneTwoNext\"), all available in high-definition. Fuji Television is owned by Fuji Media Holdings, Inc. (株式会社フジ・メディア・ホールディングス, Kabushiki-gaisha Fuji Media Hōrudingusu) and affiliated with the Fujisankei Communications Group. The current Fuji Television was established in 2008. Fuji Media Holdings is the former Fuji Television founded in 1957.",
        "genre": genres.GENERAL
    },
    TBS: {
        "id": TBS,
        "name": "TBS",
        "description": "Tokyo Broadcasting System Television, Inc. (Japanese: 株式会社TBSテレビ, Hepburn: Kabushiki-gaisha TBS Terebi) is a TV station in the Kantō region, wholly owned by Tokyo Broadcasting System Holdings. It has a 28-affiliate news network called Japan News Network (JNN). TBS produced the Takeshi's Castle game show, which is dubbed and rebroadcast internationally. The channel is also home to Ultraman and the Ultra Series franchise from 1966 onwards – itself a spinoff to Ultra Q, co-produced and broadcast in the same year – and its spinoffs, most if not all made by Tsuburaya Productions for the network. Since the 1990s it is home to Sasuke (Ninja Warrior), whose format would inspire similar programs outside Japan, by itself a spinoff to the legendary TBS game show Kinniku Banzuke that lasted for 7 seasons. On May 24, 2017, Six major media firms, including TBS, officially announced they will jointly establish a new company in July 2017 to offer paid online video services. TBS Holdings will become the largest shareholder of the new company, Premium Platform Japan, with a 31.5 percent stake. An official from TBS Holdings will become the new company's president.",
        "genre": genres.GENERAL
    },
    TOKYOMX: {
        "id": TOKYOMX,
        "name": "Tokyo MX",
        "description": "Tokyo Metropolitan Television Broadcasting Corporation (東京メトロポリタンテレビジョン株式会社, Tōkyō Metoroporitan Terebijon Kabushiki-gaisha, Tokyo MX, after its call letters, JOMX-DTV) is a television station in Tokyo, Japan. It is the only television station that exclusively serves the city. It competes with Nippon Television, TV Asahi, NHK, Tokyo Broadcasting System, TV Tokyo, and Fuji Television, all of which are flagship stations of national networks. Tokyo MX was founded on April 30, 1993, and broadcasts commenced on November 1, 1995. Shareholders include the Tokyo Metropolitan Government, Tokyo FM Broadcasting, and others (MXTV is an associate company of Tokyo FM.) Every week, Tokyo MX airs the press conferences of the Governor of Tokyo. It is a member of the Japanese Association of Independent Television Stations (JAITS).",
        "genre": genres.GENERAL
    },
    TOKYOMX2: {
        "id": TOKYOMX2,
        "name": "Tokyo MX2",
        "description": "Tokyo MX2, began broadcasting in April 2014. The channel operates on the second sub-channel of Tokyo MX1 and is primarily dedicated to alternative programming.",
        "genre": genres.BUSINESS
    },
    NHK_WORLD: {
        "id": NHK_WORLD,
        "name": "NHK World Japan",
        "description": "NHK WORLD-JAPAN is the international service of Japan's public media organization NHK. It provides the latest information on Japan and Asia through television, radio and online to a global audience.",
        "genre": genres.DOCUMENTARY
    },
    ANIMAX: {
        "id": ANIMAX,
        "name": "Animax",
        "description": "Animax Broadcast Japan Inc. (Japanese: アニマックス, Hepburn: Animakkusu), stylized as ANIMAX, is a Japanese anime satellite television network, dedicated to broadcasting anime programming. The channel also dubbed cartoons in Japanese language. A subsidiary of Sony Pictures Entertainment Japan and Mitsui & Co.'s joint venture AK Holdings, it is headquartered in New Pier Takeshiba North Tower in Minato, Tokyo, Japan, with its co-founders and shareholders including Sony Pictures Entertainment Japan and the noted anime studios Sunrise, Toei Animation, TMS Entertainment and production company NAS. Animax is the first and largest 24-hour network in the world dedicated to anime.",
        "genre": genres.ANIMES
    },
    GUNMA: {
        "id": GUNMA,
        "name": "Gunma",
        "description": "Gunma Television Co., Ltd. is a specified terrestrial broadcasting company that operates as a television broadcasting company targeting the Gunma Prefecture. Sometimes abreviated as GTV, its nickname is Gunma Television.",
        "genre": genres.LOCAL
    },
    NTV_NEWS: {
        "id": NTV_NEWS,
        "name": "NTV News 24",
        "description": "NTV NEWS24 is a news site of Nippon Television that provides the latest news with videos 24 hours a day. We will inform you about breaking news, weather forecasts, earthquakes, tsunamis, typhoons, etc.",
        "genre": genres.NEWS
    },
    WEATHER_NEWS: {
        "id": WEATHER_NEWS,
        "name": "Weather News",
        "description": "From daily life to disasters, we will deliver the most, latest, and fastest weather information. With weather reports from 2.5 million weather reporters nationwide, you can quickly grasp not only the current weather but also the impact of natural disasters on your life. In addition, it is full of fun and informative information such as seasonal information such as cherry blossoms, fireworks, autumn leaves, and slopes, earthquakes, tsunamis, typhoons, lightning strikes, and warnings.",
        "genre": genres.NEWS
    },
    NHK: {
        "id": NHK,
        "name": "NHK General",
        "description": "NHK General TV (NHK総合テレビジョン, NHK Sōgō Terebijon) is the main television service of NHK (the Japan Broadcasting Corporation). Its programming includes news, drama, quiz/variety shows, music, sports, anime, and specials which compete directly with the output of its commercial counterparts. The channel is well known for its nightly newscasts, regular documentary specials, and popular historical dramas. Among the programs NHK General TV broadcasts are the annual New Year's Eve spectacular Kōhaku Uta Gassen, the year-long Taiga drama, and the daytime Asadora. The name is often abbreviated in Japanese to Sōgō Terebi (総合テレビ) (\"GTV\" and \"NHK G\" are also used). The word Sōgō (general) serves to differentiate the channel from NHK's other television services, NHK Educational TV , NHK BS 1, NHK BS 2 (closed in 2011) and NHK BS HI (changed to BS Premium) Launched on 1 February 1953, NHK was Japan's only television channel prior to the launch of Nippon TV on 28 August 1953. NHK's programs are produced in accordance with the Japan Broadcasting Corporation Broadcasting Code.",
        "genre": genres.GENERAL
    },
    TVASAHI: {
        "id": TVASAHI,
        "name": "TV Asahi",
        "description": "TV Asahi Corporation (株式会社テレビ朝日, Kabushiki-gaisha Terebi Asahi), also known as EX and Tele-Asa (テレ朝, Tere Asa), is a Japanese television network with its headquarters in Roppongi, Minato, Tokyo, Japan. The company also owns All-Nippon News Network.",
        "genre": genres.GENERAL
    },
    TVTOKYO: {
        "id": TVTOKYO,
        "name": "TV Tokyo",
        "description": "TV Tokyo Corporation (or TX) (株式会社テレビ東京, Kabushiki-gaisha Terebi Tōkyō) TYO: 9413 is a television station headquartered in Roppongi, Minato, Tokyo, Japan majorly controlled by Nikkei, Inc. Also known as \"Teleto\" (テレ東, Teretō), a blend of \"terebi\" and \"Tokyo\", it is the flagship station of TX Network. It is one of the major Tokyo television stations, particularly specializing in anime.",
        "genre": genres.GENERAL
    },
    ATX: {
        "id": ATX,
        "name": "AT-X",
        "description": "AT-X (アニメシアターX, Anime Shiatā Ekkusu, lit. \"Anime Theater X\") is a Japanese anime television network owned by AT-X, Inc. (株式会社エー・ティー・エックス, Kabushiki kaisha Ē-Tī-Ekkusu). AT-X, Inc. was founded on June 26, 2000 as a subsidiary of TV Tokyo Medianet, which, in turn, is a subsidiary of TV Tokyo. Its headquarters are in Minato, Tokyo. AT-X network has been broadcasting anime via satellite and cable since December 24, 1997. Their slogan is Wan ranku ue no anime senmon chan'neru (ワンランク上のアニメ専門チャンネル, lit. \"Anime Specialty Channels Up a Notch\"). AT-X is always the main channel for many Comic Gum Anime adaptions. Ikkitousen, Amaenaideyo!! and Fight Ippatsu! Juuden-chan! were shown on this channel first, before they were re-aired on Tokyo MX. As a premium channel AT-X is also known for showing uncensored versions of several anime like Fight Ippatsu! Jūden-chan!!, Amaenaideyo!!, Girls Bravo, Elfen Lied, Mahoromatic and High School DxD which would normally get censored on TV-stations like TV-Tokyo because of the large amount of nudity and other factors.",
        "genre": genres.ANIMES
    },
    JAPANEWS: {
        "id": JAPANEWS,
        "name": "JapaNews 24",
        "description": "What is happening in Japan now? From current affairs such as incidents, politics, and natural disasters to city trends. Every 30 minutes, we send a program that summarizes the hot news, focusing on the events in Japan. (Reconstructed from news broadcast within a few hours in Japan.)",
        "genre": genres.NEWS
    },
    BSASAHI: {
        "id": BSASAHI,
        "name": "BS Asahi",
        "description": "TV Asahi Corporation (株式会社テレビ朝日, Kabushiki-gaisha Terebi Asahi), also known as EX and Tele-Asa (テレ朝, Tere Asa), is a Japanese television network with its headquarters in Roppongi, Minato, Tokyo, Japan. The company also owns All-Nippon News Network.",
        "genre": genres.GENERAL
    },
    BSFUJI: {
        "id": BSFUJI,
        "name": "BS Fuji TV",
        "description": "Fuji Television Network, Inc. (株式会社フジテレビジョン, Kabushiki gaisha Fuji Terebijon) is a Japanese television station based in Odaiba, Minato, Tokyo, Japan, also known as Fuji TV (フジテレビ, Fuji Terebi) or CX, based on the station's call sign \"JOCX-DTV\". It is the flagship station of the Fuji News Network (FNN) and the Fuji Network System. It is also known for its long-time slogan, \"If it's not fun, it's not TV!\" Fuji Television also operates three premium television stations, known as \"Fuji TV One\" (\"Fuji TV 739\"—sports/variety), \"Fuji TV Two\" (\"Fuji TV 721\"—drama/anime), and \"Fuji TV Next\" (\"Fuji TV CSHD\"—live premium shows) (called together as \"Fuji TV OneTwoNext\"), all available in high-definition. Fuji Television is owned by Fuji Media Holdings, Inc. (株式会社フジ・メディア・ホールディングス, Kabushiki-gaisha Fuji Media Hōrudingusu) and affiliated with the Fujisankei Communications Group. The current Fuji Television was established in 2008. Fuji Media Holdings is the former Fuji Television founded in 1957.",
        "genre": genres.GENERAL
    },
    BSTVTOKYO: {
        "id": BSTVTOKYO,
        "name": "BS TV Tokyo",
        "description": "TV Tokyo Corporation (or TX) (株式会社テレビ東京, Kabushiki-gaisha Terebi Tōkyō) TYO: 9413 is a television station headquartered in Roppongi, Minato, Tokyo, Japan majorly controlled by Nikkei, Inc. Also known as \"Teleto\" (テレ東, Teretō), a blend of \"terebi\" and \"Tokyo\", it is the flagship station of TX Network. It is one of the major Tokyo television stations, particularly specializing in anime.",
        "genre": genres.GENERAL
    },
    ETERE: {
        "id": ETERE,
        "name": "NHK Educational",
        "description": "NHK Educational TV (NHK教育テレビジョン, NHK Kyōiku terebijon), abbreviated on-screen as NHK E, is the second television service of NHK (Japan Broadcasting Corporation). It is a sister service of NHK General TV, showing programs of a more educational, cultural or intellectual nature, periodically also showing anime, and also airing programming from Nickelodeon. A similar counterpart would be PBS (Public Broadcasting Service) of the United States (or to a lesser extent BBC Two and BBC Four of the UK). NHK displays a watermark \"NHK E\" at the upper right for its digital TV broadcast. In 2010, NHK began using the abbreviation E Tele (Eテレ, Ī Tere).",
        "genre": genres.EDUCATION
    },
    BSNHK: {
        "id": BSNHK,
        "name": "NHK BS1",
        "description": "NHK (Japanese: 日本放送協会, Hepburn: Nippon Hōsō Kyōkai/Nihon Hōsō Kyōkai), also called Japan Broadcasting Corporation, is Japan's public broadcaster. NHK, which has always been known by this romanized initialism in Japanese, is a statutory corporation funded by viewers' payments of a television license fee.",
        "genre": genres.GENERAL
    },
    BSNHKPREMIUM: {
        "id": BSNHKPREMIUM,
        "name": "NHK BS Premium",
        "description": "NHK (Japanese: 日本放送協会, Hepburn: Nippon Hōsō Kyōkai/Nihon Hōsō Kyōkai), also called Japan Broadcasting Corporation, is Japan's public broadcaster. NHK, which has always been known by this romanized initialism in Japanese, is a statutory corporation funded by viewers' payments of a television license fee.",
        "genre": genres.GENERAL
    },
    BS11: {
        "id": BS11,
        "name": "BS Eleven",
        "description": "Nippon BS Broadcasting Corporation (日本BS放送株式会社, Nippon Bīesu Hōsō Kabushiki Gaisha) is a private satellite broadcasting station in Kanda, Tokyo, Japan. It is an independent television station and is a subsidiary of Bic Camera. Its channel name is BS11 (BS Eleven) and was BS11 Digital until March 31, 2011. It was founded as Nippon BS Broadcasting Kikaku (日本BS放送企画株式会社, Nippon Bīesu Hōsō Kikaku Kabushiki Kaisha) on August 23, 1999, changed its name to Nippon BS Broadcasting on February 28, 2007 and high-definition television broadcasts commenced on December 1, 2007.  BS11 gives high priority to news programs, sports, Korean drama, TV Show, anime including late night anime and 3D television programs.",
        "genre": genres.ANIMES
    },
    BSNTV: {
        "id": BSNTV,
        "name": "BS NTV",
        "description": "JOAX-DTV, virtual channel 4 (UHF digital channel 25), branded as Nippon TV, is the flagship station of the Nippon Television Network System, owned-and-operated by the Nippon Television Network Corporation which is a subsidiary of the certified broadcasting holding company Nippon Television Holdings, Inc., itself a listed subdisiary of The Yomiuri Shimbun Holdings, Japan's largest media conglomerate by revenue and the second largest behind Sony; Nippon Television Holdings forms part of Yomiuri's main television broadcasting arm alongside Kansai region flagship Yomiuri Telecasting Corporation, which owns a 6.4% share in the company.  Nippon TV's studios are located in the Shiodome area of Minato, Tokyo, Japan and its transmitters are located in the Tokyo Skytree. Broadcasting terrestrially across Japan, the network is sometimes contracted to Nittere (日テレ), and abbreviated as \"NTV\" or \"AX\". It is also the first commercial TV station in Japan, and it has been broadcasting on Channel 4 since its inception. Nippon Television is the home of the syndication networks NNN (for news programs) and NNS (for non-news programs). Except for Okinawa Prefecture, these two networks cover the whole of Japan.",
        "genre": genres.GENERAL
    },
    BSTBS: {
        "id": BSTBS,
        "name": "BS TBS",
        "description": "BS-TBS, Inc. (株式会社ビーエス・ティービーエス, Kabushiki-Gaisha Bīesu-Tībīesu) is a Japanese satellite broadcasting station headquartered in Akasaka Gochome, Minato, Tokyo. Its channel name is BS-TBS (formerly, BS-i). It is a member television station of Japan News Network.",
        "genre": genres.GENERAL
    },
    BSFUJITV: {
        "id": BSFUJITV,
        "name": "BS Fuji TV",
        "description": "Fuji Television Network, Inc. (株式会社フジテレビジョン, Kabushiki gaisha Fuji Terebijon) is a Japanese television station based in Odaiba, Minato, Tokyo, Japan, also known as Fuji TV (フジテレビ, Fuji Terebi) or CX, based on the station's call sign \"JOCX-DTV\". It is the flagship station of the Fuji News Network (FNN) and the Fuji Network System. It is also known for its long-time slogan, \"If it's not fun, it's not TV!\" Fuji Television also operates three premium television stations, known as \"Fuji TV One\" (\"Fuji TV 739\"—sports/variety), \"Fuji TV Two\" (\"Fuji TV 721\"—drama/anime), and \"Fuji TV Next\" (\"Fuji TV CSHD\"—live premium shows) (called together as \"Fuji TV OneTwoNext\"), all available in high-definition. Fuji Television is owned by Fuji Media Holdings, Inc. (株式会社フジ・メディア・ホールディングス, Kabushiki-gaisha Fuji Media Hōrudingusu) and affiliated with the Fujisankei Communications Group. The current Fuji Television was established in 2008. Fuji Media Holdings is the former Fuji Television founded in 1957.",
        "genre": genres.GENERAL
    },
    QVC: {
        "id": QVC,
        "name": "QVC",
        "description": "QVC is an American free-to-air television network, and flagship shopping channel specializing in televised home shopping, owned by Qurate Retail Group.",
        "genre": genres.SHOPPING
    },
    SHOPCHANNEL: {
        "id": SHOPCHANNEL,
        "name": "Shop Channel",
        "description": "Shop Channel is a channel specializing in television shopping. It is operated by Jupiter Shop Channel, the largest in the domestic (national) industry.",
        "genre": genres.SHOPPING
    },
    GAKINOTSUKAI: {
        "id": GAKINOTSUKAI,
        "name": "Gaki no Tsukai",
        "description": "Downtown no Gaki no Tsukai ya Arahende!! (ダウンタウンのガキの使いやあらへんで!!, Dauntaun no Gaki no Tsukai ya Arahende!!, lit. \"Downtown's We Aren't Errand Boys!\"), often abbreviated Gaki no Tsukai (ガキの使い) or just Gaki Tsuka (ガキ使), is a Japanese variety show hosted by popular Japanese owarai duo, Downtown, with comedian Hōsei Tsukitei (formerly known as Hōsei Yamasaki) and owarai duo Cocorico co-hosting. The program has been broadcast on Nippon TV since its pilot episode on October 3, 1989 and continues to this day, celebrating its 1000th episode on April 18, 2010. The program currently broadcasts on Nippon TV and its regional affiliates from 23:25 until 23:55 JST.",
        "genre": genres.ENTERTAINMENT
    },
    JAPANET: {
        "id": JAPANET,
        "name": "Japanet Channel DX",
        "description": "Japanet Takata Co., Ltd. is a Japanese company headquartered in Hiucho, Sasebo City, Nagasaki Prefecture. Japanet Channel DX (Japanet Channel Deluxe) is a channel that can be viewed by subscribing to SKY PerfecTV! Premium Service and some cable TV.",
        "genre": genres.SHOPPING
    },
    HIROSHIMAHOME: {
        "id": HIROSHIMAHOME,
        "name": "Hiroshima Home Television",
        "description": "Hiroshima Home Television Co.,Ltd. (株式会社広島ホームテレビ, Kabushiki Gaisha Hiroshima Hōmu Terebi, callsign: JOGM-TV), a.k.a. HOME (ホーム, Hōmu) is a TV station in Hiroshima. It is a network TV station of ANN. It is broadcast in Hiroshima Prefecture.",
        "genre": genres.LOCAL
    },
    ANIMETV: {
        "id": ANIMETV,
        "name": "AnimeTV",
        "description": "A 24/24 anime streaming service",
        "genre": genres.ANIMES
    },
    ANIPLUS: {
        "id": ANIPLUS,
        "name": "Aniplus",
        "description": "Aniplus is a South Korean television channel and anime distributor. Launched on 7 December 2009, the channel is currently available on SK Broadband, LG Uplus IPTV service, and KT SkyLife. The company also has a video on demand platform in its own country. Most of its programming are licensed from its parent company JJ MediaWorks for subtitling and dubbing distribution. Aniplus Asia is a Southeast Asian anime pay television channel and anime distributor based in Singapore. Founded on 25 November 2013, it is available in Singapore, Hong Kong, Indonesia and Thailand.",
        "genre": genres.ANIMES
    },
    GAORA: {
        "id": GAORA,
        "name": "GAORA Sports",
        "description": "GAORA Co., Ltd. (GAORA INCORPORATED) is a satellite backbone broadcaster that operates the sports channel GAORA SPORTS. It is a consolidated subsidiary of MBS Media Holdings [Note 1] [Note 2]. It broadcasts on SKY PerfecTV! (110 degree east longitude CS broadcast), and supplies programs to SKY PerfecTV! Premium Service, cable television, Hikari TV, etc. Organized around world sports such as soccer, American football, tennis, and Yoshimoto Kogyo's laughter programs, including the Hanshin Tigers game and the Hokkaido Nippon-Ham Fighters game of Nippon Professional Baseball. In addition to the broadcasting department, it also operates a sports community site \"SPORA\" and an online shop.",
        "genre": genres.SPORTS
    },
    JSPORTS1: {
        "id": JSPORTS1,
        "name": "J Sports 1",
        "description": "J Sports is a group of four sports satellite TV channels in Japan produced and broadcast by Jupiter Sports. They are owned by J Sports Corporation (株式会社ジェイ・スポーツ)",
        "genre": genres.SPORTS
    },
    JSPORTS2: {
        "id": JSPORTS2,
        "name": "J Sports 2",
        "description": "J Sports is a group of four sports satellite TV channels in Japan produced and broadcast by Jupiter Sports. They are owned by J Sports Corporation (株式会社ジェイ・スポーツ)",
        "genre": genres.SPORTS
    },
    JSPORTS3: {
        "id": JSPORTS3,
        "name": "J Sports 3",
        "description": "J Sports is a group of four sports satellite TV channels in Japan produced and broadcast by Jupiter Sports. They are owned by J Sports Corporation (株式会社ジェイ・スポーツ)",
        "genre": genres.SPORTS
    },
    JSPORTS4: {
        "id": JSPORTS4,
        "name": "J Sports 4",
        "description": "J Sports is a group of four sports satellite TV channels in Japan produced and broadcast by Jupiter Sports. They are owned by J Sports Corporation (株式会社ジェイ・スポーツ)",
        "genre": genres.SPORTS
    },
    KANSAITV: {
        "id": KANSAITV,
        "name": "Kansai TV",
        "description": "JODX-DTV, virtual channel 8 (UHF digital channel 17), branded as Kansai TV (関西テレビ, Kansai-terebi) or Kantele (カンテレ), is the Kansai region key station of the Fuji News Network (FNN) and Fuji Network System (FNS), operated by the Kansai Television Company Limited (関西テレビ放送株式会社, Kansai Terebi Hōsō kabushiki gaisha). Kansai TV is a company affiliated in Hankyu Hanshin Holdings Group of Hankyu Hanshin Toho Group.",
        "genre": genres.LOCAL
    },
    MAINICHIBS: {
        "id": MAINICHIBS,
        "name": "MBS TV",
        "description": "JOOY-DTV, virtual channel 4 (UHF digital channel 16), branded as MBS TV (MBSエムビーエステレビ, Emubīesu Terebī) (formerly Mainichi Broadcasting System Television (毎日放送テレビ, Mainichi Hōsō Terebi) until 23 July 2011), is the Kansai region key station of the Japan News Network, owned by Mainichi Broadcasting System, Inc.",
        "genre": genres.GENERAL
    },
    TVOSAKA: {
        "id": TVOSAKA,
        "name": "MBS TV",
        "description": "Television Osaka, Inc. (テレビ大阪株式会社, Terebi Ōsaka Kabushiki Gaisha, also referred to as TVO) is a TV station affiliated with TXN in Osaka, Japan. The mascot character is \"Takoru-kun\" (たこるくん).",
        "genre": genres.LOCAL
    },
    WAKUWAKU: {
        "id": WAKUWAKU,
        "name": "WAKUWAKU JAPAN",
        "description": "WakuWaku Japan (stylized as WAKUWAKU JAPAN) is a Japanese pay television channel that broadcasts Japanese programs to overseas viewers in Asia. The channel broadcasts only Japanese programs for 24 hours a day. Malay, Mandarin, and English language versions of these programs are broadcast on this channel. Subtitles and dubbing are available in some countries. WakuWaku Japan provides programs in various genres of anime, superhero dramas, live-action dramas, culture programs and entertainment programs.",
        "genre": genres.GENERAL
    }
}
