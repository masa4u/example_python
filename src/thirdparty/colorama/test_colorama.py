from colorama import Fore, Back, Style


def print_fore():
    # print dir(Fore)
    for key in dir(Fore):
        if not key.startswith('_'):
            fore_color = getattr(Fore, key)
            print '%s Hello Fore : %s' % (fore_color, key)

def print_back():
    # print dir(Back)
    for key in dir(Back):
        if not key.startswith('_'):
            back_color = getattr(Back, key)
            print '%s Hello Back : %s' % (back_color, key)

def print_style():
     for key in dir(Style):
        if not key.startswith('_'):
            back_color = getattr(Style, key)
            print '%s Hello Style : %s' % (back_color, key)


print print_fore()
# print print_back()
print print_style()