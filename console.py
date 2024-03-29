#!/usr/bin/python3

'''
Module for Console
'''

import cmd


class HBNBCommand(cmd.Cmd):
    ''' this class represents the Console
    '''

    prompt = '(hbnb) '

    def do_EOF(self, line):
        ''' method for EOF'''
        return True

    def do_quit(self, line):
        ''' Quit command to exit the program'''
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
