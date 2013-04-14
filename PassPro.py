from itertools import product
from optparse import OptionParser

class PassPro(object):
    
    def __init__(self, user_input):
        self.user_input = user_input
        self.alphabet = {'a': 'aA@4', 'b': 'bB8', 'c': 'cC(', 'd': 'dD', 'e': 'eE3', \
                 'f': 'fF', 'g': 'gG69', 'h': 'h#H', 'i': 'iI1l', 'j': 'j;J', \
                 'k': 'kKxX', 'l': 'lL!1', 'm': 'mM', 'n': 'nN', 'o': 'oO0', 'p': 'pP', \
                 'q': 'qQ', 'r': 'rR', 's': 's5S$', 't': 'tT!+7', 'u': 'uU', \
                 'v': 'vV', 'w': 'wW', 'x': 'xX', 'y': 'yY', 'z': 'z2Z'}

        self.output = product(*map(self.alphabet.get, self.user_input))
        
        self.parser = OptionParser()
        self.parser.add_option('-f', '--file', dest = 'filename',
                          help = 'read in from FILE', metavar='FILE')
        (self.opts, self.args) = self.parser.parse_args()
        if self.opts.filename:
            self.read_file(self.opts.filename)
        

    def read_file(self, args):
        print 'stuff'
    def help(self):
        pass
    def generator(self):
        pass
    def walker(self):
        pass
    def custom(self):
        pass
    
        
        
    
               
        
#user_input = raw_input('gimme: ')
#user_input = user_input.lower()
password = PassPro('a')

#for i in password.output:
    #print ''.join(i)