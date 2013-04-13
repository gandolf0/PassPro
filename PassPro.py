from itertools import product

class PassPro(object):
    
    def __init__(self, user_input):
        self.user_input = user_input
        self.alphabet = {'a': 'aA@4', 'b': 'bB8', 'c': 'cC(', 'd': 'dD', 'e': 'eE3', \
                 'f': 'fF', 'g': 'gG9', 'h': 'hH', 'i': 'iI1l', 'j': 'jJ', \
                 'k': 'kKxX', 'l': 'lL!1', 'm': 'mM', 'n': 'nN', 'o': 'oO0', 'p': 'pP', \
                 'q': 'qQ', 'r': 'rR', 's': 'sS$', 't': 'tT!+7', 'u': 'uU', \
                 'v': 'vV', 'w': 'wW', 'x': 'xX', 'y': 'yY', 'z': 'zZ'}

        self.output = product(*map(self.alphabet.get, self.user_input))
               
        
user_input = raw_input('gimme: ')
user_input = user_input.lower()
password = PassPro(user_input)

for i in password.output:
    print ''.join(i)