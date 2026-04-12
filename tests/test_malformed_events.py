def test_invalid_event_structure():
    from app.events.validators import validate_event

    bad_event = {"wrong": "format"}

    assert validate_event(bad_event) is False
