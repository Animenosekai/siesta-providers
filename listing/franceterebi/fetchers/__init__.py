"""
Here is a list of fetchers for Japan Terebi

The `fetch` function in each file should return the sources for each channel.

Returns
-------
dict[str, list[tuple[str, Any]]]
    > Example
    {
        "channel_id": [
            ("source", {"header1": "value1"})
        ]
    }
"""
from siesta.server.utils.request import Session, SharedSession
from . import iptvorg

FETCHERS = [
    iptvorg,
]


def fetch(session: Session = SharedSession):
    data = {}

    for fetcher in FETCHERS:
        for channel, links in fetcher.fetch(session).items():
            try:
                data[channel].extend(links)
            except Exception:
                data[channel] = links

    return data
