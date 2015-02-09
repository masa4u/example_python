import contextlib

@contextlib.contextmanager
def make_context(name):
    print 'entering:', name
    yield name
    print 'exiting :', name

with contextlib.nested(make_context('A'), make_context('B'), make_context('C')) as (A, B, C):
    print 'inside with statement:', A, B, C