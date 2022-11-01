import datetime
import json

from bs4 import BeautifulSoup
from bson import ObjectId
from siesta.sdk.providers.models import BaseMetadataProvider, Provider
from siesta.server.utils import finder

from .graphql import ID_ANIME_QUERY


def desc(value: str):
    if value is None:
        return None
    value = " ".join(BeautifulSoup(value, "html.parser").find_all(text=True, recursive=True))
    # value = value.replace("<br>", "\n")
    return value


class AniList(Provider):
    NAME = "AniList"
    DESCRIPTION: str = "Search through the thousands of animes available on AniList.co to add metadata"

    class MetadataProvider(BaseMetadataProvider):
        def get_title(self, titles: dict, synonyms: list = None):
            title = titles.get("romaji", None)
            if title is None:
                title = titles.get("native", None)
            if title is None:
                title = titles.get("english", None)
            if title is None and synonyms is not None:
                try:
                    title = synonyms[0]
                except IndexError:
                    pass
            if title is None:
                raise ValueError("We couldn't find the title for the given media")
            return title

        def anilist_to_siesta(self, media: dict):
            if media.get("type", "") == "MANGA" or media.get("format") in ["MANGA", "NOVEL", "ONE_SHOT"]:
                raise ValueError("The given media seems to be a manga")
            titles = media.get("title", {})
            title = self.get_title(titles, synonyms=media.get("synonyms", []))
            tags = [t.get("name") for t in media.get("tags", [])]
            tags.extend(media.get("synonyms", []))
            tags.extend([titles.get(t) for t in ["romaji", "native", "english"]])
            tags.extend(media.get("genres", []))
            tags.append(media.get("country"))

            tags = [finder.tokenize(t) for t in tags if t is not None]

            related = []
            for edge in media.get("related", {}).get("edges", []):
                node = edge.get("node", {})
                t = node.get("title", {})
                found = finder.find_media({
                    "title": self.get_title(t, synonyms=media.get("synonyms", [None])),
                    "identifiers": {
                        "anilist": node.get("anilist"),
                        "mal": node.get("mal"),
                        "_anilist_romaji": finder.tokenize(t.get("romaji")),
                        "_anilist_native": finder.tokenize(t.get("native")),
                        "_anilist_english": finder.tokenize(t.get("english")),
                    }
                })
                if found is None:
                    continue
                related.append({
                    "_id": found._id,
                    "relation": edge.get("relation", "OTHER")
                })

            characters = []
            for edge in media.get("characters", {}).get("edges", []):
                node = edge.get("node")
                name = node.get("name", {})

                try:
                    va = edge.get("voiceActors", [{}])[0]
                except Exception:
                    va = {}
                va_name = va.get("name", {})

                result = {
                    "name": name.get("romaji", name.get("native")),
                    "image": node.get("image", {}).get("large"),
                    "description": desc(node.get("description")),
                    "actor": va_name.get("romaji", va_name.get("native")),
                    "actor_image": va.get("image", {}).get("large"),
                    "identifiers": {
                        "anilist": node.get("anilist"),
                        "_anilist_romaji": finder.tokenize(name.get("romaji")),
                        "_anilist_native": finder.tokenize(name.get("native")),
                    }
                }

                current = finder.find_character(result)
                if current is None:
                    char_id = ObjectId()
                    self.characters[char_id] = result
                else:
                    current = finder.merge_characters(current, result)
                    char_id = current["_id"]
                characters.append({"_id": char_id, "role": str(edge.get("role", "BACKGROUND")).upper()})

            reviews = [{
                "title": rev.get("title"),
                "reviewer": rev.get("user", {}).get("reviewer"),
                "content": desc(rev.get("content")),
                "url": rev.get("url")
            } for rev in media.get("reviews", {}).get("nodes", [])[:10]]  # limit to 10

            studios = [s.get("node").get("name") for s in media.get("studios", {}).get("edges", []) if s.get("isMain", False)]
            if len(studios) <= 0:
                studios = [s.get("node").get("name") for s in media.get("studios", {}).get("edges", []) if s.get("node").get("name")]

            release = media.get("release", None)
            release = datetime.datetime(
                year=release.get("year") or 1970,
                month=release.get("month") or 1,
                day=release.get("day") or 1
            )

            url = None
            links = media.get("links", [])
            for link in links:
                try:
                    if "officialsite" in finder.tokenize(str(link.get("site"))):
                        url = link["url"]
                        break
                except Exception:
                    continue
            else:
                for link in links:
                    try:
                        if link.get("type") == "INFO":
                            url = link["url"]
                            break
                    except Exception:
                        continue
                else:
                    for link in links:
                        try:
                            if link.get("type") == "SOCIAL":
                                url = link["url"]
                                break
                        except Exception:
                            continue
                    else:
                        try:
                            url = links[0]["url"]
                        except Exception:
                            pass

            return {
                "title": title,
                "genres": media.get("genres", []),
                "tags": tags,
                "studios": studios,
                "related": related,
                "characters": characters,
                "reviews": reviews,
                "poster": media.get("poster", {}).get("large"),
                "banner": media.get("banner"),
                "release": release.timestamp(),
                "description": desc(media.get("description")),
                "age": 18 if (media.get("hentai", False) or "nudity" in tags) else (16 if "ecchi" in tags else None),
                "hyouka": media.get("hyouka"),
                "url": url,
                "type": "MOVIE" if media.get("format") == "MOVIE" else "SERIES",
                "identifiers": {
                    "anilist": media["anilist"],
                    "mal": media.get("mal"),
                    "_anilist_romaji": finder.tokenize(titles.get("romaji")),
                    "_anilist_native": finder.tokenize(titles.get("native")),
                    "_anilist_english": finder.tokenize(titles.get("english"))
                }
            }

        def find(self, id: int):
            r = self.session.request("POST", "https://graphql.anilist.co/", json={
                "query": ID_ANIME_QUERY,
                "variables": {
                    "id": int(id)
                }
            })
            r.raise_for_status()
            result = r.json()["data"]["Media"]
            return self.anilist_to_siesta(result)

        def dump(self, obj: dict, output: str):
            obj = obj.copy()

            obj["related"] = [{
                "_id": str(r["_id"]),
                "relation": str(r["relation"])
            } for r in obj.get("related", [])]

            characters = []
            for char in obj.get("characters", []):
                data = self.characters[char["_id"]]
                characters.append({
                    "role": char.get("role", "BACKGROUND"),
                    "name": data["name"],
                    "image": data.get("image"),
                    "description": desc(data.get("description")),
                    "actor": data.get("actor"),
                    "actor_image": data.get("actor_image"),
                    "identifiers": data.get("identifiers", {})
                })
            obj["characters"] = characters

            with open(output, "w") as f:
                f.write(json.dumps(obj, ensure_ascii=False, separators=(",", ":")))
