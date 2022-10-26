import pathlib

from siesta.sdk.importer import absolute_import

Bangumis = {}

for channel in pathlib.Path(__file__).parent.iterdir():
    if not channel.name.endswith(".py"):
        continue
    if channel.name == "__init__.py":
        continue
    name = channel.name.removesuffix(".py")
    Bangumis[name] = absolute_import(pathlib.Path(__file__).parent / channel.name)
