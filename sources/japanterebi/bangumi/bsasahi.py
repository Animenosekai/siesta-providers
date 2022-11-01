
import pathlib

from siesta.sdk.importer import absolute_import

jcom = absolute_import(pathlib.Path(__file__).parent / "jcom.py")
from siesta.server.utils.request import Session, SharedSession

LOCATION = 3
SERVICE_CODE = "151_4"


def retrieve(session: Session = SharedSession):
    return jcom.retrieve(SERVICE_CODE, location=LOCATION, session=session)
