def test_make_event():
    from app.events.schemas import make_event

    event = make_event("test.topic", {"key": "value"})

    event_dict = event.to_dict()

    assert event_dict["topic"] == "test.topic"
    assert "event_id" in event_dict
    assert "timestamp" in event_dict
    assert event_dict["payload"]["key"] == "value"
