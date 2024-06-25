import redis


def get_redis_connection() -> redis.Redis:
    return redis.Redis(host='localhost', port=6379, db=0)


def set_pom_count():
    redis = get_redis_connection()
    redis.set("pom_count", 1)