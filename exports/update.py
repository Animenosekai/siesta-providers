import argparse
import json
import pathlib
import re

from nasse.utils.sanitize import remove_spaces
from siesta.sdk.console import console
from siesta.cli.installer import TempProvider

INPUT_CLEANUP_REGEX = re.compile(r"\(.+\)")


def normalize(string: str):
    return remove_spaces(INPUT_CLEANUP_REGEX.sub("", string.lower()))


def main(output: pathlib.Path, directory: pathlib.Path):
    directory = pathlib.Path(directory)

    SEARCH_LISTING = {}
    AUTHORS_LISTING = {}

    for item in directory.iterdir():
        try:
            if item.is_dir():
                try:
                    data = json.loads((item / "metadata.siesta.json").read_text())
                except Exception:
                    with TempProvider(item / "source.siesta") as temp_provider:
                        data = temp_provider.build_info

                # Search
                SEARCH_LISTING[normalize(data["id"])] = data["id"]
                SEARCH_LISTING[normalize(data["name"])] = data["id"]
                AUTHORS_LISTING[normalize(data.get("author", "Siesta Community"))] = data.get("author", "Siesta Community")
        except Exception:
            console.print_exception()
            continue

    (output / "search.json").write_text(json.dumps(SEARCH_LISTING, ensure_ascii=False, separators=(",", ":")))
    (output / "authors.json").write_text(json.dumps(AUTHORS_LISTING, ensure_ascii=False, separators=(",", ":")))


if __name__ == "__main__":
    parser = argparse.ArgumentParser("siesta-analytics", description="Updates the analytics database")
    parser.add_argument("dir", action="store", help="The directory to analyze")
    parser.add_argument("--output", "-o", action="store", required=False, type=pathlib.Path,
                        help="The outputting directory.")

    args = parser.parse_args()
    main(output=args.output or pathlib.Path(), directory=args.dir)
