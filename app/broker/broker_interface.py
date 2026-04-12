from typing import Callable, Protocol


class BrokerInterface(Protocol):
    def publish(self, topic: str, event: dict) -> None:
        ...

    def subscribe(self, topic: str, handler: Callable[[dict], None]) -> None:
        ...
