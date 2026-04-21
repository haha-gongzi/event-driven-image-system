from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any, Dict
import uuid


@dataclass
class Event:
    type: str
    topic: str
    event_id: str
    timestamp: str
    payload: Dict[str, Any]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def make_event(topic: str, payload: Dict[str, Any]) -> Event:
    return Event(
        type="publish",
        topic=topic,
        event_id=f"evt_{uuid.uuid4().hex[:12]}",
        timestamp=datetime.now(timezone.utc).isoformat(),
        payload=payload,
    )
