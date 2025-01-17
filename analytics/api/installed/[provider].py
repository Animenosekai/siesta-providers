import time

from db.db import mongo
from nasse import Dynamic, Endpoint, Nasse, RequestProxy

nasse_app = Nasse("SiestaProviders", debug=False, log_file=None)

RATE_LIMIT = {}
INSTALL_LIMIT = 60

LOCAL_CACHE = {}
CACHE_EXPIRATION = 60  # in seconds


@nasse_app.route('/<path:path>', endpoint=Endpoint(
    name="Installed Providers",
    description={
        "GET": "Returns the total number of installs",
        "POST": "Adds an installation to the counter"
    },
    methods=["GET", "POST"],
    dynamics=Dynamic("provider", "The provider to search for", required=False)
))
def installed(request: RequestProxy, method: str, provider: str):
    provider = provider.replace(".", "-")  # avoid `.` mongodb paths

    if method == "POST":
        install_rl_key = f"{provider}@{request.client_ip}"

        last_call = RATE_LIMIT.get(install_rl_key, 0)
        if time.time() - last_call <= INSTALL_LIMIT:
            return 429, f"Intalls within {INSTALL_LIMIT} seconds are considered as one install"
        RATE_LIMIT[install_rl_key] = time.time()

        try:
            mongo[provider].installs.append(int(time.time()))
        except (KeyError, AttributeError):
            return 404, "Couldn't find the given provider"

        return 200, "Successfully added your install to the counter"

    cached = LOCAL_CACHE.get(provider, {"t": 0, "r": 0})
    try:
        if time.time() - cached["t"] <= CACHE_EXPIRATION:
            return 200, {"installs": cached["r"]}
    except Exception:
        nasse_app.logger.debug("An error occured while getting the local cache")

    try:
        result = len(mongo[provider].installs)
    except KeyError:
        return 404, "Couldn't find the given provider"
    LOCAL_CACHE[provider] = {"t": time.time(), "r": result}

    return 200, {"installs": result}


# Exposing the underlying Flask app
app = nasse_app.flask
