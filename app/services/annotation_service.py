from app.broker.redis_broker import RedisBroker
from app.events.schemas import make_event
from app.events.topics import ANNOTATION_STORED
from app.storage.document_store import DocumentStore


store = DocumentStore()


def handle_inference_completed(event):
    broker = RedisBroker()

    image_id = event["payload"]["image_id"]
    event_id = event["event_id"]

    annotation = {
        "image_id": image_id,
        "objects": event["payload"].get("objects", []),
    }

    
    saved = store.save_annotation(event_id, image_id, annotation)

    if not saved:
        print(f"Duplicate event ignored: {event_id}")
        return

    
    new_event = make_event(ANNOTATION_STORED, annotation)
    broker.publish(ANNOTATION_STORED, new_event.to_dict())
