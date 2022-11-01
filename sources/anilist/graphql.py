Identifier = """
fragment Identifier on Media {
  anilist: id
  mal: idMal
  title {
    romaji # title
    native # take if romaji is null
    english # take if native is null
  }
}
"""

MediaInfo = """
fragment MediaInfo on Media {
  ...Identifier
  synonyms # tags
  hentai: isAdult # if 18+ or not
  poster: coverImage {
    # color
    large: extraLarge
  }
  tags {
    name
    # rank
  }
  type
  format # verify if MOVIE or SERIES
  banner: bannerImage
  release: startDate {
    year
    month
    day
  }
  description(asHtml: false)
  genres
  synonyms # as tags
  hyouka: averageScore
  country: countryOfOrigin # as a tag
  related: relations {
    edges {
      relation: relationType(version: 2)
      node {
        ...Identifier
      }
    }
  }
  characters(sort: [ROLE, RELEVANCE, ID]) {
    edges {
      role
      voiceActors(language: JAPANESE, sort: [RELEVANCE, ID]) {
        name {
          romaji: full
          native # take this one if romaji is null
        }
        image {
          large
        }
      }
      node {
        anilist: id
        name {
          romaji: full
          native # use this one if romaji is null
        }
        image {
          large
        }
        description(asHtml: false)
      }
    }
  }
  studios {
    edges {
      isMain # only save main studios
      node {
        name
      }
    }
  }
  reviews(sort: [RATING_DESC, ID]) {
    nodes {
      title: summary # title
      user {
        reviewer: name # reviewer
      }
      content: body(asHtml: false) # content
      url: siteUrl # url?
    }
  }
  links: externalLinks { # for "url?"
    site # Official Sites first
    url
    type # sort
  }
}
"""

ID_ANIME_QUERY = Identifier + MediaInfo + """
query ($id: Int) {
  Media(id: $id, type: ANIME) {
    ...MediaInfo
  }
}
"""

SEARCH_ANIME_QUERY = Identifier + """
query ($search: String) {
    anime: Page(perPage: 10) {
        results: media(type: ANIME, search: $search) {
          ...Identifier
        }
    }
}
"""