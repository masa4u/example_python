import abc

class Base(object):
    __metaclass__ = abc.ABCMeta

    def value_getter(self):
        return 'Should never see this'

    def value_setter(self, newvalue):
        return

    value = abc.abstractproperty(value_getter, value_setter)


class PartialImplementation(Base):

    @abc.abstractproperty
    def value(self):
        return 'Read-only'


class Implementation(Base):

    _value = 'Default value'

    def value_getter(self):
        return self._value

    def value_setter(self, newvalue):
        self._value = newvalue

    value = property(value_getter, value_setter)


class ReadOnlyImplementation(PartialImplementation):
    @property
    def value(self):
        return 'AAAAAAAAAAA'

try:
    b = Base()
    print 'Base.value:', b.value
except Exception, err:
    print 'Base.value ERROR:', str(err)

try:
    p = PartialImplementation()
    print 'PartialImplementation.value:', p.value
except Exception, err:
    print 'PartialImplementation.value ERROR:', str(err)

i = Implementation()
print 'Implementation.value:', i.value

i.value = 'New value'
print 'Changed value:', i.value

p = ReadOnlyImplementation()
print p.value
