from app.broker.redis_broker import RedisBroker
from app.events.schemas import make_event
from app.events.topics import INFERENCE_COMPLETED, ANNOTATION_STORED
from app.events.validators import validate_event

def handle_inference_completed(event: dict) -> None:
    print("Annotation service received:", event)

    if not validate_event(event):
        print("Invalid event")
        return

    payload = event["payload"]
    image_id = payload["image_id"]

    # analog storage annotation
    annotation = {
        "image_id": image_id,
        "annotations": payload["objects"],
        "status": "stored"
    }

    new_event = make_event(
        ANNOTATION_STORED,
        annotation
    )

    broker = RedisBroker()
    broker.publish(ANNOTATION_STORED, new_event.to_dict())

    print(f"Stored annotation for {image_id}")

def main():
    broker = RedisBroker()
    print("Annotation service listening on inference.completed...")
    broker.subscribe(INFERENCE_COMPLETED, handle_inference_completed)

if __name__ == "__main__":
    main()
