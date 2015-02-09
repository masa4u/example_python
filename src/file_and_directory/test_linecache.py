import linecache

# Look for the linecache module, using
# the built in sys.path search.
module_line = linecache.getline('test_linecache.py', 3)
print '\nMODULE : ', module_line