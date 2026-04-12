import json
from typing import Callable, Dict
import redis


class RedisBroker:
    def __init__(self, host: str = "localhost", port: int = 6379, db: int = 0):
        self.client = redis.Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True
        )

    def publish(self, topic: str, event: dict) -> None:
        """
        Publish an event to a Redis topic
        """
        self.client.publish(topic, json.dumps(event))

    def subscribe(self, topic: str, handler: Callable[[Dict], None]) -> None:
        """
        Subscribe to a Redis topic and handle incoming events
        """
        pubsub = self.client.pubsub()
        pubsub.subscribe(topic)

        for message in pubsub.listen():
            if message["type"] == "message":
                data = json.loads(message["data"])
                handler(data)
