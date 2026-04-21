from typing import Callable, Protocol


class BrokerInterface(Protocol):
    def publish(self, topic: str, event: dict) -> None:
        """Publish an event to a topic"""
        ...

    def subscribe(self, topic: str, handler: Callable[[dict], None]) -> None:
        """Subscribe to a topic with a handler"""
        ...
