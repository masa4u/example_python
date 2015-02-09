import test_threading



thr = test_threading.Thread(target=foo, args=(), kwargs={})
thr.start()

thr.is_alive()

thr.join()