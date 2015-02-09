# System modules
from Queue import Queue
from threading import Thread
import time

# Set up some global variables
num_fetch_threads = 4
enclosure_queue = Queue()

# A real app wouldn't use hard-coded data...
sources = ['http://www.castsampler.com/cast/feed/rss/guest',
           'http://masa.cguru.org',
           'http://daum.net',
           'http://naver.com'
           ]

def queue_worker(i, q):
    """This is the worker thread function.
    It processes items in the queue one after
    another.  These daemon threads go into an
    infinite loop, and only exit when
    the main thread ends.
    """
    while True:
        print '%s: Looking for the next enclosure' % i
        url = q.get()
        print '%s: Downloading:' % i, url
        # do something
        print 'WORKING!!'
        time.sleep(i + 2)
        q.task_done()

# Set up some threads to fetch the enclosures
for i in range(num_fetch_threads):
    t = Thread(target=queue_worker, args=(i, enclosure_queue,))
    t.setDaemon(True)
    t.start()

# Download the feed(s) and put the enclosure URLs into
# the queue.
for url in sources:
    enclosure_queue.put(url)

# Now wait for the queue to be empty, indicating that we have
# processed all of the downloads.
print '*** Main thread waiting'
enclosure_queue.join()
print '*** Done'