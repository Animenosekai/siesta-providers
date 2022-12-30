from yuno import YunoClient, YunoDatabase, YunoCollection, YunoDict


class ProviderType(YunoDict):
    tv: bool
    media: bool
    metadata: bool


class Provider(YunoDict):
    _id: str  # the provider id
    installs: list[int]
    author: str
    type: ProviderType


class SiestaProvidersCollection(YunoCollection):
    __type__ = Provider

    def __getitem__(self, name: str) -> Provider:
        return super().__getitem__(name)


class SiestaProvidersDatabase(YunoDatabase):
    siesta: SiestaProvidersCollection


class SiestaProvidersClient(YunoClient):
    siesta: SiestaProvidersDatabase
