import argparse
import json
import os
import pathlib

from siesta.cli.installer import TempProvider
from siesta.sdk.console import console

from analytics.db.models import SiestaProvidersClient


def main(mongo_uri: str, directory: pathlib.Path):
    directory = pathlib.Path(directory)
    mongo = SiestaProvidersClient(mongo_uri).siesta.siesta

    for item in directory.iterdir():
        try:
            if item.is_dir():
                try:
                    data = json.loads((item / "metadata.siesta.json").read_text())
                except Exception:
                    with TempProvider(item / "source.siesta") as temp_provider:
                        data = temp_provider.build_info

                type_data = data.get("type", {})
                document = mongo[data["id"]]
                document.author = data.get("author", "Siesta Community")
                document.type = {
                    "tv": type_data.get("tv", False),  # type: ignore
                    "media": type_data.get("media", False),
                    "metadata": type_data.get("metadata", False),
                }

        except Exception:
            console.print_exception()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("siesta-analytics", description="Updates the analytics database")
    parser.add_argument("dir", action="store", help="The directory to analyze")
    parser.add_argument("--mongo-uri", action="store", required=False, type=pathlib.Path,
                        help="The MongoDB instance URI to use. If not specified, the `SIESTA_MONGO_URI` environment variable will be used.")

    args = parser.parse_args()
    main(mongo_uri=args.mongo_uri or os.environ.get("SIESTA_MONGO_URI", ""), directory=args.dir)
