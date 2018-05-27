import redis

def set_redis_cli(host='localhost', port=6379):
    return redis.Redis(host, port)

def enqueue(self, key, value):
    #key_enq  = key if key else self.key
    pass

def dequeue(redis_cli):
    if not isinstance(redis_cli, redis.Redis):
        raise

    return redis_cli.lpop

