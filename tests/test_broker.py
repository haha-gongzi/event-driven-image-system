from unittest.mock import MagicMock, patch

from app.broker.redis_broker import RedisBroker


def test_broker_publish_calls_redis_client_publish():
    broker = RedisBroker()
    broker.client = MagicMock()

    event = {"type": "publish", "topic": "test.topic", "payload": {"msg": "hello"}}
    broker.publish("test.topic", event)

    broker.client.publish.assert_called_once()


@patch("app.services.cli_service.RedisBroker")
def test_cli_submit_image_publishes_event(mock_broker_cls):
    from app.services.cli_service import submit_image

    mock_broker = MagicMock()
    mock_broker_cls.return_value = mock_broker

    submit_image("img_001", "images/test1.jpg", "cli")

    mock_broker.publish.assert_called_once()
    called_topic, called_event = mock_broker.publish.call_args[0]

    assert called_topic == "image.submitted"
    assert called_event["topic"] == "image.submitted"
    assert called_event["payload"]["image_id"] == "img_001"
    assert called_event["payload"]["path"] == "images/test1.jpg"
