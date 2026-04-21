from app.events.topics import IMAGE_SUBMITTED
from app.events.validators import validate_event


def test_invalid_event_missing_fields():
    bad_event = {
        "topic": IMAGE_SUBMITTED,
        "payload": {"image_id": "img_001"},
    }
    assert validate_event(bad_event) is False


def test_invalid_event_wrong_type():
    bad_event = {
        "type": "not_publish",
        "topic": IMAGE_SUBMITTED,
        "event_id": "evt_123",
        "timestamp": "2026-04-21T10:00:00Z",
        "payload": {"image_id": "img_001"},
    }
    assert validate_event(bad_event) is False


def test_invalid_event_wrong_payload_type():
    bad_event = {
        "type": "publish",
        "topic": IMAGE_SUBMITTED,
        "event_id": "evt_123",
        "timestamp": "2026-04-21T10:00:00Z",
        "payload": "not a dict",
    }
    assert validate_event(bad_event) is False


def test_invalid_event_unknown_topic():
    bad_event = {
        "type": "publish",
        "topic": "unknown.topic",
        "event_id": "evt_123",
        "timestamp": "2026-04-21T10:00:00Z",
        "payload": {"image_id": "img_001"},
    }
    assert validate_event(bad_event) is False
