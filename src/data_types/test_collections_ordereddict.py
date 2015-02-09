d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}

from collections import OrderedDict

print OrderedDict(sorted(d.items(), key=lambda t:t[0]))
