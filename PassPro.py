from itertools import product
from optparse import OptionParser

class PassPro(object):
    
    def __init__(self):
        
        self.alphabet = {'a': 'aA@4', 'b': 'bB8', 'c': 'cC(', 'd': 'dD', \
                         'e': 'eE3', 'f': 'fF', 'g': 'gG69', 'h': 'h#H', \
                         'i': 'iI1l', 'j': 'j;J', 'k': 'kKxX', 'l': 'lL!1', \
                         'm': 'mM', 'n': 'nN', 'o': 'oO0', 'p': 'pP', \
                         'q': 'qQ', 'r': 'rR', 's': 's5S$', 't': 'tT!+7', \
                         'u': 'uU', 'v': 'vV', 'w': 'wW', 'x': 'xX', \
                         'y': 'yY', 'z': 'z2Z'}
        self.cli_parse()
        
    def cli_parse(self):
        self.parser = OptionParser()
        self.parser.add_option('-g', '--generator', type = 'choice', 
                               choices = ['L', 'U', 'N', 'S', 'LU', 'LN', 'LS',
                                          'LUN', 'LNS', 'LUNS', 'UN', 'US',
                                          'NS'], 
                                          dest = 'gen_opts')
        self.parser.add_option('-f', '--file', dest = 'filename',
                               help = 'read in from FILE', metavar='FILE')
        self.parser.add_option('-v', '--verbose', action="count", 
                               dest='verbosity', default=1)
        self.parser.add_option('-q', '--quiet', action='store_const', 
                               const=0, dest='verbosity')
        self.parser.add_option('-w', '--word', dest = 'user_input', 
                               help = 'convert a password into every variant')
        
        (self.opts, self.args) = self.parser.parse_args()
        
        if self.opts.filename:
            self.read_file(self.opts.filename)
        elif self.opts.gen_opts:
            if self.opts.gen_opts == 'L':
                print 'im the L option'
            ## add other ifs for the options or handle it in a function
        elif self.opts.user_input:
            self.stuff = self.output_words(self.opts.user_input)
            for i in self.stuff:
                print ''.join(i)
        
    def read_file(self, args):
        print 'read_file'
    def help(self):
        print 'help'
    def generator(self):
        print 'generator'
    def walker(self):
        print 'walker'
    def custom(self):
        print 'custom'
    def output_words(self, user_input):
        self.user_input = user_input
        return product(*map(self.alphabet.get, self.user_input))
        
password = PassPro()
