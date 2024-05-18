#! /bin/env python3
from redis import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

r.hset('user:jessica', mapping={
    'name'; 'jessica',
'passwd': 'password'
})
u = h.hgetall('user:jessica')



