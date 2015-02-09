'''http://pymotw.com/2/cmd/'''

import cmd

class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    intro = 'simple command processor'
    prompt = 'command :'
    def do_greet(self, line):
        print "hello"

    def do_EOF(self, line):
        return True

if __name__ == '__main__':
    HelloWorld().cmdloop()