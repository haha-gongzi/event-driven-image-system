from app.broker.redis_broker import RedisBroker
from app.events.schemas import make_event
from app.events.topics import QUERY_COMPLETED

def handle_query(event):
    broker = RedisBroker()

    query = event["payload"]["query"]

    
    results = {
        "query": query,
        "results": ["img_001", "img_002"]
    }

    new_event = make_event(QUERY_COMPLETED, results)
    broker.publish(QUERY_COMPLETED, new_event.to_dict())