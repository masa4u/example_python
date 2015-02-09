import eventlet
eventlet.monkey_patch()

pool = eventlet.GreenPool()

target = {}
for x in range(0,100):
    target[x] = x
import time
import random
def square(x):
    print x, x*x
    time.sleep(4)


for key, value in target.items():
    pool.spawn_n(square, key)
    pool.waitall()
