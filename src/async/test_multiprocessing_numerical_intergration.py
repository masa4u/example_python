from test_multiprocessing_simple import async
from multiprocessing import Pool
from random import sample
from math import log

@async
def random_async():
    p = range(1, 90000)
    rlt = 1
    for x in p:
        rlt += log(p)
    return rlt
def random_sync():
    p = range(1, 9000000)
    rlt = 1
    for x in p:
        rlt += log(p)
    return rlt


if __name__ == '__main__':
    from random import sample
    import timeit

    def case_async(pool_size):
        # The process pool must be created inside __main__.
        async.pool = Pool(pool_size)

        results = []
        for i in range(4):
            results.append(random_async())
        return results

    def case_sync():
        results = []
        for i in range(4):
            results.append(random_sync())
        return results

    for pool_size in range(1, 8):
        start = timeit.default_timer()
        rlts = case_async(pool_size)
        stop = timeit.default_timer()
        async_time = stop - start

        for rlt in rlts:
            if rlt.successful():
                print rlt.get()
            else:
                print 'fail'
        print ('pool_size=%d async=%f rlt=%f' % (pool_size, async_time))

    start = timeit.default_timer()
    case_async(2)
    stop = timeit.default_timer()
    async_time = stop - start
    print ('async=%f' % (async_time))

    # start = timeit.default_timer()
    # case_sync()
    # stop = timeit.default_timer()
    # sync_time = stop - start

    # print ('sync=%f' % (sync_time))