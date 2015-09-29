from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage
import json

def pp24_simplesuper(name, position):
    redis_publisher = RedisPublisher(facility='foobar', broadcast=True)
    data = json.dumps({'field1': name, 'field2': position})
    message = RedisMessage(data)
    # and somewhere else
    redis_publisher.publish_message(message)
