from app.storage.document_store import DocumentStore


def test_duplicate_event_not_saved_twice():
    store = DocumentStore()

    event_id = "evt_123"
    image_id = "img_001"
    data = {"label": "cat"}

    first = store.save_annotation(event_id, image_id, data)
    second = store.save_annotation(event_id, image_id, data)

    assert first is True
    assert second is False
