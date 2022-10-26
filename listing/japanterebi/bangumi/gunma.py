import pathlib

from siesta.sdk.importer import absolute_import
from siesta.server.utils.request import Session, SharedSession

mcas = absolute_import(pathlib.Path(__file__).parent / "mcas.py")


def retrieve(session: Session = SharedSession):
    return mcas.retrieve(8, session=session)
