from app.events.schemas import make_event
from app.events.topics import IMAGE_SUBMITTED
from app.events.validators import validate_event


def test_make_event_contains_required_fields():
    event = make_event(
        IMAGE_SUBMITTED,
        {
            "image_id": "img_001",
            "path": "images/test1.jpg",
            "source": "cli",
        },
    )

    event_dict = event.to_dict()

    assert event_dict["type"] == "publish"
    assert event_dict["topic"] == IMAGE_SUBMITTED
    assert isinstance(event_dict["event_id"], str)
    assert event_dict["event_id"].startswith("evt_")
    assert isinstance(event_dict["timestamp"], str)
    assert isinstance(event_dict["payload"], dict)


def test_make_event_is_valid_by_validator():
    event = make_event(
        IMAGE_SUBMITTED,
        {
            "image_id": "img_001",
            "path": "images/test1.jpg",
            "source": "cli",
        },
    )

    assert validate_event(event.to_dict()) is True
