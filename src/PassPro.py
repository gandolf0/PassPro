#!/usr/bin/python
from itertools import chain, product
from optparse import OptionParser
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from hashlib import new
from binascii import hexlify
import re

'''
-- TODO --
fix crack method (research samdump format)
-- END --
'''

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
                           'L': ascii_lowercase, 'U': ascii_uppercase,
                           'N': digits, 'S': punctuation,}
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
                                          'LUN', 'LUS', 'LNS', 'LUNS', 'UN', 'US',
                                          'NS'], dest = 'gen_opts', 
                               help = 'brute force generator (requires -l)', metavar = 'ARGS')
        self.parser.add_option('-k', '--walker', dest = 'walker_opts', 
                               help = 'keyboard pattern generator',
                               metavar = 'ARGS')
        self.parser.add_option('-H', '--cracker', dest = 'hash', 
                               help = 'hash cracker, uses local word list',
                               metavar = 'HASH')
        self.parser.add_option('-l', '--length', dest = 'length', 
                               help = 'option of length for generator (required with -g and -c)',
                               metavar = 'NUM')
        self.parser.add_option('-c', '--custom', 
                               help = 'custom character set for generator (requires -l)',
                               dest = 'customize', metavar = 'FILE')
        self.parser.add_option('-v', '--verbose', action="count", 
                               dest='verbosity', default = 1, 
                               help = 'set verbosity level')
        self.parser.add_option('-q', '--quiet', action='store_const', 
                               const=0, dest='verbosity', 
                               help = 'suppress verbosity')
        
        (self.opts, self.args) = self.parser.parse_args()
        
        if self.opts.filename: # -f 
            self.read_file(self.opts.filename)
        elif self.opts.user_input: # -w
            output_object = self.output_words(self.opts.user_input)
            for i in output_object:
                print ''.join(i)           
        elif self.opts.gen_opts and self.opts.length: # -g
            gen_obj = self.generator(self.opts.gen_opts, self.opts.length)
            for i in gen_obj:
                print i    
        elif self.opts.walker_opts and self.opts.length: # -k 
            self.walker(self.opts.walker_opts, self.opts.length)
        elif self.opts.customize and self.opts.length: # -c
            cust_obj = self.custom(self.opts.customize, self.opts.length)
            for i in cust_obj:
                print i
        elif self.opts.hash: # -H
                self.crack(self.opts.hash)
        else: # no options
            print self.parser.get_usage()
        
    def read_file(self, args):
        
        open_file = open(args)
        for word in open_file:
            #raw_input('Press Enter to continue:  ')
            output_object = self.output_words(word.strip('\n'))
            for mangle in output_object:
                print ''.join(mangle)
        open_file.close()
        
    def help(self):
        print 'help'
        
    def generator(self, gen_sets, length):
        ''' Generates every possible combination of generic character sets with a given length '''
        set_list = []
        for option in gen_sets:
            set_list.append(self.alpha_sets.get(option))
        chars = ''.join(set_list)
        return (''.join(combination) for combination in 
                chain.from_iterable(product(chars, repeat=i) 
                                              for i in range(1, int(length) + 1)))
    def custom(self, chars, length):
        ''' Generates every possible combination of user-defined character sets with a given length '''
        return (''.join(combination) for combination in 
                chain.from_iterable(product(chars, repeat=i) 
                                              for i in range(1, int(length) + 1)))
            
    def walker(self, walker_sets, length):
        ''' Walks the keyboard in pre-defined patterns with user-defined length '''
        length = int(length)
        orig_len = length
        while length % 4 != 0:
            length += 1
        length = length / 4
        
        walker = self.alpha_sets.get(walker_sets)
        temp_list = []
        try:
            for i in xrange(len(walker)):
                for j in xrange(length):
                    temp_list.append(walker[i + j])
                word = ''.join(temp_list)
                print word[:orig_len]
                temp_list = []   
        except IndexError:
            pass
        
    def output_words(self, user_input):
        ''' Mangles the word given with the included dictionary '''
        return product(*map(self.alphabet.get, user_input))
    
    def crack(self, user_input):
        
        ''' 
        need to take a look at lanman hashes and see how they'd be C&P'd into a file.
        right now the hashes ive used are all below 8 characters because of how 
        i built them.  Once i know how the lanmans are handled by the samdump, 
        I can figure out how to process ones that are longer than 8 chars
        '''
        
        word_list = open('ComboFile.txt')
        print '** If you entered a single hash through the CLI, leave the file entry blank. **'
        user_file = raw_input('Please specify the file of hashes you\'d like to crack: ')
        CRACKED = False 
        try:
            input_file = open(user_file)
            while not CRACKED:
                for hash in input_file:
                    hash = hash.strip('\n')
                    groups = re.split(':', hash)
                    user = groups[0]
                    hash_1 = groups[2]
                    hash_2 = groups[3]
                    for line in word_list:
                        line = line.strip('\n')
                        if len(line) <= 8:
                            hashed_pw = hexlify(new('md4', line.encode('utf-16le')).digest()).upper()
                            if hashed_pw == hash_1:
                                hash_1 = line
                                word_list.seek(0)
                            elif hashed_pw == hash_2:
                                hash_2 = line
                                word_list.seek(0)
                            if len(hash_1) < 32 and len(hash_2) < 32:
                                print '[*]', user + ':', hash_1 + hash_2
                                word_list.seek(0)
                                CRACKED = True
                                break
                        else:
                            first_half = line[:8]
                            second_half = line[8:]
                            first_hash = hexlify(new('md4', first_half.encode('utf-16le')).digest()).upper()
                            second_hash = hexlify(new('md4', second_half.encode('utf-16le')).digest()).upper()
                            if first_hash == hash_1 or second_hash == hash_2:
                                print '[*]', user + ':', first_half
                                print '[*]', user + ':', second_half
                                break
                            ## need an end of file handler
                    
        except IOError:
            for line in word_list:
                line = line.strip('\n')
                #print 'line is', line, 'and is', len(line), 'long'
                if len(line) <= 8:
                    #print '========in the if========'
                    hashed_pw = hexlify(new('md4', line.encode('utf-16le')).digest()).upper()
                    if hashed_pw == user_input:
                        print 'The password is', line
                else:
                    #print '********in the else*********'
                    first_half = line[:8]
                    second_half = line[8:]
                    first_hash = hexlify(new('md4', first_half.encode('utf-16le')).digest()).upper()
                    second_hash = hexlify(new('md4', second_half.encode('utf-16le')).digest()).upper()
                    if first_hash == user_input or second_hash == user_input:
                        print 'The first part of the password is', first_half
                        print 'The second part of the password is', second_half
                        
        word_list.close()
    
        
password = PassPro()
