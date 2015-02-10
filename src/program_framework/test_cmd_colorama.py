'''http://pymotw.com/2/cmd/'''

import cmd
from colorama import Fore, Back

class HelloWorldColorama(cmd.Cmd):
    """
    Simple command processor example.
    """
    intro = 'simple command processor'
    prompt = Fore.YELLOW + 'H(help): ' + Fore.WHITE

    def do_greet(self, line):
        print "hello"

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorldColorama().cmdloop()