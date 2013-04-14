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
        self.alpha_sets = {'A': ['!QAZ', '1qaz', 'ZAQ!', 'zaq1', '@WSX', \
                                 '2wsx', "XSW@","xsw2","#EDC","3edc","CDE#", \
                                 "cde3", "$RFV","4rfv","VFR$","vfr4","%TGB", \
                                 "5tgb", "BGT%","bgt5","^YHN","6yhn","NHY^", \
                                 "nhy6"],
                           'B': ['!@', '@!', "QW", "WQ", "AS", "SA", "ZX", \
                                 "XZ", "12", "21", "qw", "wq", "as", "sa", \
                                 "zx", "xz", "@#", "#@", "WE", "EW", "SD", \
                                 "DS", "XC", "CX", "23", "32", "we", "ew", \
                                 "sd", "ds", "xc", "cx", "#$", "$#", "ER", \
                                 "RE", "DF", "FD", "CV", "VC", "34", "43", \
                                 "er", "re", "df", "fd", "cv", "vc", "$%", \
                                 "%$", "RT", "TR", "FG", "GF", "VB", "BV", \
                                 "45", "54", "rt", "tr", "fg", "gf", "vb", \
                                 "bv"],
                           'C': ['!QAZ', "1qaz", "ZAQ!", "zaq1", "@WSX", \
                                 "2wsx", "XSW@", "xsw2", "#EDC", "3edc", \
                                 "CDE#", "cde3", '$RFV', 'VFR$', 'vfr4', \
                                 '%TGB', '5tgb', 'BGT%', 'bgt5', '^YHN', \
                                 '6yhn', 'NHY^', 'nhy6', "&UJM", "mju7", \
                                 "*IK<", ",ki8", "(OL>", ".lo9", ")P:?", \
                                 "/;p0"],
                           'D': ["!QW@", "@WQ!", "1qw2", "2wq1", "@WE#", \
                                 "#EW@", "2we3", "3ew2", "#ER$", "$RE#", \
                                 "3er4", "4re3", "$RT%", "%TR$", "4rt5", \
                                 "5tr4", "%TY^", "^YT%", "5ty6", "6yt5"],
                           'L': 'abcdefghijklmnopqrstuvwxyz', 
                           'U': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                           'N': '1234567890', 
                           'S': '~`!@#$%^&*()-_+=[]\{}|;:",./<>?\''}
        self.cli_parse()
        
    def cli_parse(self):
        usage = 'usage: %prog [options] args'
        self.parser = OptionParser(usage = usage)
        self.parser.add_option('-f', '--file', dest = 'filename',
                               help = 'read in from FILE', metavar='FILE')
        self.parser.add_option('-w', '--word', dest = 'user_input',
                               help = 'read a word from STDIN',
                               metavar = 'STDIN')
        self.parser.add_option('-g', '--generator', type = 'choice', 
                               choices = ['L', 'U', 'N', 'S', 'LU', 'LN', 'LS',
                                          'LUN', 'LNS', 'LUNS', 'UN', 'US',
                                          'NS'], dest = 'gen_opts', 
                               help = 'brute force generator', metavar = 'ARGS')
        self.parser.add_option('-k', '--walker', dest = 'walker_opts', 
                               help = 'keyboard pattern generator',
                               metavar = 'ARGS')
        self.parser.add_option('-c', '--custom', 
                               help = 'check for file with custom variables',
                               dest = 'customize', metavar = 'FILE')
        self.parser.add_option('-v', '--verbose', action="count", 
                               dest='verbosity', default = 1, 
                               help = 'set verbosity level')
        self.parser.add_option('-q', '--quiet', action='store_const', 
                               const=0, dest='verbosity', 
                               help = 'suppress verbosity')
        
        (self.opts, self.args) = self.parser.parse_args()
        
        if self.opts.filename: ## -f 
            self.read_file(self.opts.filename)
        elif self.opts.user_input: ## -w
            self.output_object = self.output_words(self.opts.user_input)
            for i in self.output_object:
                print ''.join(i)
        elif self.opts.gen_opts: ## -g
                self.generator(self.opts.gen_opts)
        elif self.opts.walker_opts: ## -k 
            self.walker(self.opts.walker_opts)
        elif self.opts.customize: ## -c
            self.custom(self.opts.customize)
        else: ## no options
            print self.parser.get_usage()
        
    def read_file(self, args):
        print 'read_file'
    def help(self):
        print 'help'
    def generator(self, gen_sets):
        print 'generator'
    def walker(self, walker_sets):
        print 'walker'
    def custom(self, customize):
        print 'custom'
    def output_words(self, user_input):
        self.user_input = user_input
        return product(*map(self.alphabet.get, self.user_input))
        
password = PassPro()
