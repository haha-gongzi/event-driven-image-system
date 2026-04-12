from app.broker.redis_broker import RedisBroker
from app.events.schemas import make_event
from app.events.topics import IMAGE_SUBMITTED, INFERENCE_COMPLETED
from app.events.validators import validate_event


def handle_image_submitted(event: dict) -> None:
    print("Received event:", event)

    # check the 'event'
    if not validate_event(event):
        print("Invalid event received")
        return

    payload = event["payload"]
    image_id = payload["image_id"]

    # simulate inference
    inferred_objects = [
        {"label": "car", "bbox": [10, 20, 100, 120], "conf": 0.95},
        {"label": "person", "bbox": [130, 50, 180, 200], "conf": 0.89},
    ]

    completed_event = make_event(
        INFERENCE_COMPLETED,
        {
            "image_id": image_id,
            "model_version": "mock-v1",
            "objects": inferred_objects,
        },
    )

    broker = RedisBroker()
    broker.publish(INFERENCE_COMPLETED, completed_event.to_dict())

    print(f"Processed image {image_id} → inference.completed")


def main() -> None:
    broker = RedisBroker()
    print("Inference service listening on image.submitted...")
    broker.subscribe(IMAGE_SUBMITTED, handle_image_submitted)


if __name__ == "__main__":
    main()
