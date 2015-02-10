# import colored import fg, bg, attr
from colorama import Fore, Back

print 'normal'
print ('%s Hello World !!! %s' % (Fore.BLUE + Back.BLACK, Fore.RED))
print ('%s Hello World !!! %s' % (Fore.BLUE + Back.WHITE, Fore.RED))
print Fore.RED + 'dddfd'
print 'dddfd' + Fore.BLUE