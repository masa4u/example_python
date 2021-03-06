'''
http://pymotw.com/2/SimpleXMLRPCServer/index.html#module-SimpleXMLRPCServer
'''
from SimpleXMLRPCServer import SimpleXMLRPCServer
import logging
import os

# Set up logging
logging.basicConfig(level=logging.DEBUG)

server = SimpleXMLRPCServer(('localhost', 9000), logRequests=True)

# Expose a function
def list_contents(dir_name):
    logging.debug('list_contents(%s)', dir_name)
    print os.listdir(dir_name)
    return os.listdir(dir_name)
server.register_function(list_contents)

try:
    print 'Use Control-C to exit'
    server.serve_forever()
except KeyboardInterrupt:
    print 'Exiting'