from app.broker.redis_broker import RedisBroker
from app.events.schemas import make_event
from app.events.topics import IMAGE_SUBMITTED


def submit_image(image_id: str, path: str, source: str = "cli") -> None:
    broker = RedisBroker()

    event = make_event(
        IMAGE_SUBMITTED,
        {
            "image_id": image_id,
            "path": path,
            "source": source,
        },
    )

    broker.publish(IMAGE_SUBMITTED, event.to_dict())

    print(f"Published image.submitted for {image_id}")


if __name__ == "__main__":
    submit_image("img_001", "images/test1.jpg")
