def test_broker_publish_does_not_crash():
    from app.broker.redis_broker import RedisBroker

    broker = RedisBroker()

    broker.publish("test.topic", {"msg": "hello"})

    assert True
