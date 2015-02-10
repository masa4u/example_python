"""http://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example"""


#classes are objects too
def make_myklass(**kwattrs):
    return type('MyKlass', (object,), dict(**kwattrs))

myklass_foo_bar = make_myklass(foo=2, bar=4)
print myklass_foo_bar
x = myklass_foo_bar()
print x.foo, x.bar


# what is metaclass? : class of a class(meta class)
"""
When it sees a class definition, Python executes it to collect the attributes (including methods) into a dictionary.
When the class definition is over, Python determines the metaclass of the class. Let's call it Meta
Eventually, Python executes Meta(name, bases, dct), where:
Meta is the metaclass, so this invocation is instantiating it.
name is the name of the newly created class
bases is a tuple of the class's base classes
dct maps attribute names to objects, listing all of the class's attributes
"""



# metaclass's __new__ and __init__
"""
creation and initialization of the class in the metaclass,
you can implement the metaclass's __new__ method and/or __init__ constructor [6].
Most real-life metaclasses will probably override just one of them.

__new__ should be implemented when you want to control the creation of a new object (class in our case),
and
__init__ should be implemented when you want to control the initialization of the new object
after it has been created.
"""

class MyMeta(type):
    def __new__(meta, name, bases, dct):
        print '-----------------------------------'
        print "Allocating memory for class", name
        print meta
        print bases
        print dct
        return super(MyMeta, meta).__new__(meta, name, bases, dct)
    def __init__(cls, name, bases, dct):
        print '-----------------------------------'
        print "Initializing class", name
        print cls
        print bases
        print dct
        super(MyMeta, cls).__init__(name, bases, dct)

MyKlass = MyMeta.__new__(MyMeta, name, bases, dct)
MyMeta.__init__(MyKlass, name, bases, dct)