import pathlib

from siesta.sdk.importer import absolute_import
from siesta.server.utils.request import Session, SharedSession

parser = absolute_import(pathlib.Path(__file__).parent / "parser.py")

def retrieve(session: Session = SharedSession):
    return parser.retrieve("BFMTV.fr", session=session)
