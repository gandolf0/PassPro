class PassPro(object):
    
    def __init__(self, user_input):
        self.user_input = user_input
        self.alphabet = {'a': 'aA@4', 'b': 'bB8', 'c': 'cC(', 'd': 'dD', 'e': 'eE3', \
                 'f': 'fF', 'g': 'gG9', 'h': 'hH', 'i': 'iI1l', 'j': 'jJ', \
                 'k': 'kKxX', 'l': 'lL!1', 'm': 'mM', 'n': 'nN', 'o': 'oO0', 'p': 'pP', \
                 'q': 'qQ', 'r': 'rR', 's': 'sS$', 't': 'tT!+7', 'u': 'uU', \
                 'v': 'vV', 'w': 'wW', 'x': 'xX', 'y': 'yY', 'z': 'zZ'}

        self.output = self.convert(*map(self.alphabet.get, self.user_input))        
            
    def convert(self, *args, **kwds):
        lists = map(tuple, args) * kwds.get('repeat', 1)
        result = [[]]
        for i in lists:
            result = [x+[y] for x in result for y in i]
        for j in result:
            yield tuple(j)
            
                
        
user_input = raw_input('gimme: ')
user_input = user_input.lower()
password = PassPro(user_input)

for i in password.output:
    print ''.join(i)