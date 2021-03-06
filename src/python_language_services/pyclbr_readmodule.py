import pyclbr
import os
from operator import itemgetter

def show_class(name, class_data):
    print 'Class:', name
    print '\tFile: {0} [{1}]'.format(os.path.basename(class_data.file), class_data.lineno)
    show_super_classes(name, class_data)
    show_methods(name, class_data)
    print
    return

def show_methods(class_name, class_data):
    for name, lineno in sorted(class_data.methods.items(), key=itemgetter(1)):
        print '\tMethod: {0} [{1}]'.format(name, lineno)
    return

def show_super_classes(name, class_data):
    super_class_names = []
    for super_class in class_data.super:
        if super_class == 'object':
            continue
        if isinstance(super_class, basestring):
            super_class_names.append(super_class)
        else:
            super_class_names.append(super_class.name)
    if super_class_names:
        print '\tSuper classes:', super_class_names
    return

example_data = pyclbr.readmodule('pyclbr_example')

for name, class_data in sorted(example_data.items(), key=lambda x:x[1].lineno):
    show_class(name, class_data)