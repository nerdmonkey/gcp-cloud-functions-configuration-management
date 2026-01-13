import os

import functions_framework
from dotenv import load_dotenv


def _load_local_env_if_present() -> None:
    """Load .env for local development; no-op in managed runtimes."""
    load_dotenv(override=False)


@functions_framework.cloud_event
def main(cloud_event):
    """CloudEvent-triggered function.

    Compatible with Google Cloud Functions (2nd gen) / Cloud Run + Eventarc.
    """
    _load_local_env_if_present()

    debug = os.getenv("APP_DEBUG")
    secret_key = os.getenv("SECRET_KEY")
    database_url = os.getenv("DATABASE_URL")

    # Log event metadata (helpful for debugging triggers)
    event_id = None
    event_source = None
    event_type = None

    # In Functions Framework, CloudEvent is typically dict-like (cloudevents SDK).
    if hasattr(cloud_event, "get"):
        event_id = cloud_event.get("id")
        event_source = cloud_event.get("source")
        event_type = cloud_event.get("type")
    else:
        # Fallback for alternative CloudEvent implementations.
        event_id = getattr(cloud_event, "id", None)
        event_source = getattr(cloud_event, "source", None)
        event_type = getattr(cloud_event, "type", None)

    print("event.id:", event_id)
    print("event.source:", event_source)
    print("event.type:", event_type)

    # Dump selected env vars (careful: SECRET_KEY will appear in logs)
    print("APP_DEBUG:", debug)
    print("SECRET_KEY:", secret_key)
    print("DATABASE_URL:", database_url)

    # CloudEvent functions may return a value; it's typically ignored for background events.
    return "ok"


if __name__ == "__main__":
    # Convenience: allow running as a plain script too.
    _load_local_env_if_present()
    print("APP_DEBUG:", os.getenv("APP_DEBUG"))
    print("SECRET_KEY:", os.getenv("SECRET_KEY"))
    print("DATABASE_URL:", os.getenv("DATABASE_URL"))
