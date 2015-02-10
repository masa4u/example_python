from abc import ABCMeta


class MyABC:
    __metaclass__ = ABCMeta

MyABC.register(tuple)

print MyABC
print dir(MyABC)

print issubclass(tuple, MyABC)
print isinstance((), MyABC)


class Test(MyABC):
    pass

print Test

print dir(Test)