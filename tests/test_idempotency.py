def test_event_ids_are_unique():
    from app.events.schemas import make_event

    e1 = make_event("test.topic", {"id": 1})
    e2 = make_event("test.topic", {"id": 1})

    assert e1.event_id != e2.event_id
