from app.events.topics import ALL_TOPICS


REQUIRED_FIELDS = {"type", "topic", "event_id", "timestamp", "payload"}


def validate_event(event: dict) -> bool:
    # must be dict
    if not isinstance(event, dict):
        return False

    # All fields must be included
    missing = REQUIRED_FIELDS - set(event.keys())
    if missing:
        return False

    # The 'type' must be the 'publish'
    if event["type"] != "publish":
        return False

    # The 'topic' must be valid 
    if event["topic"] not in ALL_TOPICS:
        return False

    # The 'event_id' must be a string
    if not isinstance(event["event_id"], str) or not event["event_id"]:
        return False

    # The 'timestamp' must be present
    if not isinstance(event["timestamp"], str) or not event["timestamp"]:
        return False

    # The 'payload' must be 'dict'
    if not isinstance(event["payload"], dict):
        return False

    return True
