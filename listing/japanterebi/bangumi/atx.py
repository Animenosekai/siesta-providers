import pathlib

from siesta.sdk.importer import absolute_import

jcom = absolute_import(pathlib.Path(__file__).parent / "jcom.py")
from siesta.server.utils.request import Session, SharedSession

LOCATION = 120
SERVICE_CODE = "182_65406"


def retrieve(session: Session = SharedSession):
    return jcom.retrieve(SERVICE_CODE, location=LOCATION, session=session)
