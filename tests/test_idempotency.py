from app.events.schemas import make_event


def test_generated_event_ids_are_unique():
    e1 = make_event("image.submitted", {"image_id": "img_001"})
    e2 = make_event("image.submitted", {"image_id": "img_001"})

    assert e1.event_id != e2.event_id
