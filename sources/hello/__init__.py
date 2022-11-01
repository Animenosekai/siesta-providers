from siesta.sdk.providers.models import Provider, BaseMediaProvider, BaseMetadataProvider, BaseTVProvider


class hello(Provider):
    NAME: str = "hello"
    VERSION = (0, 0, 1)
    DESCRIPTION: str = "Welcome to your future provider"

    class MediaProvider(BaseMediaProvider):
        ...

    class MetadataProvider(BaseMetadataProvider):
        ...

    class TVProvider(BaseTVProvider):
        ...
