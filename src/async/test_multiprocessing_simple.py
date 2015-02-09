from inspect import getmodule
from multiprocessing import Pool

def async(decorated):
    r'''Wraps a top-level function around an asynchronous dispatcher.

        when the decorated function is called, a task is submitted to a
        process pool, and a future object is returned, providing access to an
        eventual return value.

        The future object has a blocking get() method to access the task
        result: it will return immediately if the job is already done, or block
        until it completes.

        This decorator won't work on methods, due to limitations in Python's
        pickling machinery (in principle methods could be made pickleable, but
        good luck on that).
    '''
    # Keeps the original function visible from the module global namespace,
    # under a name consistent to its __name__ attribute. This is necessary for
    # the multiprocessing pickling machinery to work properly.
    module = getmodule(decorated)
    decorated.__name__ += '_original'
    setattr(module, decorated.__name__, decorated)

    def send(*args, **opts):
        return async.pool.apply_async(decorated, args, opts)

    return send


@async
def printsum(uid, values):
    summed = 0
    for value in values:
        summed += value

    # print("Worker %i: sum value is %i" % (uid, summed))

    return (uid, summed)

def printsum_sync(uid, values):
    summed = 0
    for value in values:
        summed += value

    # print("Worker %i: sum value is %i" % (uid, summed))

    return (uid, summed)


if __name__ == '__main__':
    from random import sample
    import timeit

    def case_async():
        # The process pool must be created inside __main__.
        async.pool = Pool(4)

        p = range(0, 1000)
        results = []
        for i in range(4):
            values = sample(p, 100)
            # print values
            result = printsum(i, values)
            results.append(result)

        # for result in results:
            # print result
            # print result.get()
            # print("Worker %i: sum value is %i" % result.get())
    def case_sync():
        results = []
        p = range(0, 1000)
        for i in range(4):
            values = sample(p, 100)
            result = printsum_sync(i, values)
            results.append(result)
        return result

    start = timeit.default_timer()
    case_async()
    stop = timeit.default_timer()
    async_time = stop - start

    start = timeit.default_timer()
    case_sync()
    stop = timeit.default_timer()
    sync_time = stop - start

    print ('aync=%f, sync=%f' % (async_time, sync_time))