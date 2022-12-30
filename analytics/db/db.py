from db.models import SiestaProvidersClient
from os import environ

mongo = SiestaProvidersClient(environ["SIESTA_MONGO_URI"]).siesta.siesta
