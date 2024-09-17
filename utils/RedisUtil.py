from redis import Redis
from config.conf import ConfigReader


class RedisUtill:

    def __init__(self):
        redis_url = ConfigReader().get_conf_redis()
        redis_db = ConfigReader().get_redis_db()
        self.rds = Redis(host=redis_url, port='6379', password='', decode_responses=True, db=redis_db)

    def rds_get(self, key):
        value = self.rds.get(key)
        return value
