import pathlib

from siesta.sdk.importer import absolute_import

nhk_guide = absolute_import(pathlib.Path(__file__).parent / "nhk_guide.py")
from siesta.server.utils.request import Session, SharedSession


def retrieve(session: Session = SharedSession):
    return nhk_guide.retrieve("s3", session=session)
