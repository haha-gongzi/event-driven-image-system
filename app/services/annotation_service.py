from app.broker.redis_broker import RedisBroker
from app.events.schemas import make_event
from app.events.topics import ANNOTATION_STORED, INFERENCE_COMPLETED
from app.events.validators import validate_event
from app.storage.document_store import DocumentStore

# Simulated document database owned by the annotation service
store = DocumentStore()


def handle_inference_completed(event: dict) -> None:
    """
    Handle an inference.completed event, store annotation results,
    and publish annotation.stored if the event is valid and new.
    """
    if not validate_event(event):
        print("Invalid event received by annotation service")
        return

    if event["topic"] != INFERENCE_COMPLETED:
        print(f"Ignoring unexpected topic: {event['topic']}")
        return

    broker = RedisBroker()

    image_id = event["payload"].get("image_id")
    event_id = event["event_id"]

    if not image_id:
        print("Missing image_id in payload")
        return

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


def main() -> None:
    """
    Start the annotation service and subscribe to inference.completed events.
    """
    broker = RedisBroker()
    print("Annotation service listening on inference.completed...")
    broker.subscribe(INFERENCE_COMPLETED, handle_inference_completed)


if __name__ == "__main__":
    main()
