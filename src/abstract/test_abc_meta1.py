from abc import ABCMeta, abstractmethod, abstractproperty


class MyAbstract(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def func_a(self):
        return

    @abstractproperty
    def readonly_property(self):
        return 'not here'

    def get_x(self):
        return self._x
    def set_x(self, value):
        self._x = 2
    x = abstractproperty(get_x, set_x)


class KKK(MyAbstract):
    def func_a(self):
        return 9

    @property
    def readonly_property(self):
        '''
        read only property

        :return:
        '''
        return 'lll'

    def get_x(self):
        return self._x
    def set_x(self, value):
        self._x = 3
    x = property(get_x, set_x)

a = KKK()

print 'KKK issubclass ' + str(issubclass(KKK, MyAbstract))
print 'KKK isinstance ' + str(isinstance(KKK, MyAbstract))
print 'a is isinstance ' + str(isinstance(a, MyAbstract))


print a.readonly_property
