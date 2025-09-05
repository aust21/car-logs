import redis

r = redis.Redis()

r.set("transmission","faulty")