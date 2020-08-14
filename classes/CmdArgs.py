import sys


class CmdArgs:

    def __init__(self):
        self.args = sys.argv

    def print_console(self):

        for arg in self.args:
            print(arg)
