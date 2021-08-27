
import redis
from untils.getConfig import getConfig


if __name__ == '__main__':
    host = getConfig('redis','host')
    pool = redis.ConnectionPool(host=host,port=6379,db=0,password='123456',)
    r = redis.StrictRedis(connection_pool=pool)
    if r.set('foo','bar'):
        print(r.get('foo'))

    r.hset()














