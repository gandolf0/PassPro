import os
import argparse
import itertools
#version 2.1
def permute_word(word):
    return itertools.product(
        *(alphabet.get(x, x) for x in word)
    )

def combine_this(stuff,num):
    for permutation in itertools.product(stuff,repeat=num):
        password = "".join(permutation)
        bail = False
        if args.requirelower:
            if not any(char in lower for char in password):
                bail = True
        if args.requireupper:
            if not any(char in upper for char in password):
                bail = True
        if args.requirenumber:
            if not any(char in numbs for char in password):
                bail = True
        if args.requirespecial:
            if not any(char in lower for char in password):
                bail = True
        if not bail:
            write_out(password)

def open_file(filename):
    cleandata = []
    if os.path.isfile(filename):
        with open(filename, "r") as f:
            data = f.readlines()
        for l in data:
            cleandata.append(l.rstrip())
        return cleandata
    else:
        print('ERROR: File not found\n')
        exit()

def write_out(data):         
    if args.output:
        with open(args.output,"a+") as f:
            f.write(data+"\n")
    else:
        print(data)

def convert_2_l33t(args):
    if args.mangle:
        pass
        #need to add stuff here.
    if args.word:
        for permutation in permute_word(args.word):
            #write_out("".join(permutation)+args.mangle)
            password = "".join(permutation)
            bail = False
            if args.requirelower:
                if not any(char in lower for char in password):
                    bail = True
            if args.requireupper:
                if not any(char in upper for char in password):
                    bail = True
            if args.requirenumber:
                if not any(char in numbs for char in password):
                    bail = True
            if args.requirespecial:
                if not any(char in lower for char in password):
                    bail = True
            if not bail:
                write_out(password)
    elif args.file:
        data = open_file(args.file)
        for word in data:
            for permutation in permute_word(word):
                #write_out("".join(permutation)+args.mangle)
                password = "".join(permutation)
                bail = False
                if args.requirelower:
                    if not any(char in lower for char in password):
                        bail = True
                if args.requireupper:
                    if not any(char in upper for char in password):
                        bail = True
                if args.requirenumber:
                    if not any(char in numbs for char in password):
                        bail = True
                if args.requirespecial:
                    if not any(char in lower for char in password):
                        bail = True
                if not bail:
                    write_out(password)

def scramble_words(args):
    data = open_file(args.file)
#   data.append('')#Maybe add a range using this to decrement for the minimum 
#   max#-min# = # of nulls to add to this list
    combine_this(data,args.num)

def walk_keyboard(args):
    if (args.set == "A" or args.set == "B" or args.set == "D") and ((args.length & 3) != 0):
        print('ERROR: Length not a multiple of four! Learn math dummy.')
    elif args.set == "C" and ((args.length & 1) != 0):
        print('ERROR: Length not a multiple of 2! Learn math dummy.')
    elif args.set == "A":
        combine_this(A,int(args.length/4))
    elif args.set == "B":
        combine_this(B,int(args.length/4))
    elif args.set == "C":
        combine_this(C,int(args.length/4))
    elif args.set == "D":
        combine_this(D,int(args.length/4))
        
def generate_words(args):
    the_list = []
    if args.lowercase:
        the_list += lower
    if args.uppercase:
        the_list += upper
    if args.numbers:
        the_list += numbs
    if args.special:
        the_list += chars
    if args.hexchar:
        the_list += hexchar    
    combine_this(the_list,args.num)

lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbs = ['1','2','3','4','5','6','7','8','9','0']
#chars = ['~','!','@','#','$','%','^','&','*','(',')','_','+','`','-','=','{','}','|','[',']','\\',':','"',';',"'",
#        '<','>','?',',','.','/']
chars = ['!','@','#','$','*','_','+','.','%']
hexchar = ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f']
alphabet = {
    "a": "aA@4",
    "b": "bB8",
    "c": "cC(",
    "d": "dD",
    "e": "eE3",
    "f": "fF",
    "g": "gG69",
    "h": "h#H",
    "i": "iI1l!",
    "j": "j;J",
    "k": "kKxX",
    "l": "lL!17",
    "m": "mM",
    "n": "nN",
    "o": "oO0",
    "p": "pP",
    "q": "qQ",
    "r": "rR",
    "s": "s5S$",
    "t": "tT!+7",
    "u": "uU",
    "v": "vV",
    "w": "wW",
    "x": "xX",
    "y": "yY",
    "z": "z2Z",
    "{": "{(<[",
    "}": "}]>)",
}

#Sets of 4, 20 Elements, Left Side 1-5
A = ["!QAZ","1qaz","ZAQ!","zaq1","@WSX","2wsx","XSW@","xsw2","#EDC","3edc",
    "CDE#","cde3","$RFV","4rfv","VFR$","vfr4","%TGB","5tgb","BGT%","bgt5"]

#Sets of 4, 40 Elements, Whole Keyboard
B = ["!QAZ","1qaz","ZAQ!","zaq1","@WSX","2wsx","XSW@","xsw2","#EDC","3edc",
    "CDE#","cde3","$RFV","4rfv","VFR$","vfr4","%TGB","5tgb","BGT%","bgt5",
    "^YHN","6yhn","NHY^","nhy6","&UJM","7ujm","MJU&","mju7","*IK<","8ik,",
    "<KI*",",ki8","(OL>","9ol.",">LO(",".lo9",")P:?","0p;/","?:P)","/;p0"]

#Sets of 2, 64 Elements, left side, 1-5
C = ["!@","@!","QW","WQ","AS","SA","ZX","XZ",
    "12","21","qw","wq","as","sa","zx","xz",
    "@#","#@","WE","EW","SD","DS","XC","CX",
    "23","32","we","ew","sd","ds","xc","cx",
    "#$","$#","ER","RE","DF","FD","CV","VC",
    "34","43","er","re","df","fd","cv","vc",
    "$%","%$","RT","TR","FG","GF","VB","BV",
    "45","54","rt","tr","fg","gf","vb","bv"]

#Sets of 4, 20 Elements, Loops on top, Whole Keyboard
D = ["!QW@","@WQ!","1qw2","2wq1","@WE#","#EW@","2we3","3ew2",
    "#ER$","$RE#","3er4","4re3","$RT%","%TR$","4rt5","5tr4",
    "%TY^","^YT%","5ty6","6yt5","^YU&","&UY^","6yu7","7uy6",
    "&UI*","*IU&","7ui8","8iu7","*IO(","(OI*","8io9","9oi8",
    "(OP)",")PO(","9op0","0po9"]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='PassPro',formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-o", "--output", help="File to save results to.",metavar='<file_path>')
    subparsers = parser.add_subparsers(help='Features of Password Producer|Professional:')
#####
    parser_L = subparsers.add_parser('leet',formatter_class=argparse.RawTextHelpFormatter,help='The L33t Converter:\n'
            '  This option will convert provided words to every permutation of leet speak.\n'
            ' '
            )
    parser_L.add_argument("-m", "--mangle", help="Add a manglinger to the end of the password.(Comma seperated)",metavar='<2022,123!>',default='')
    parser_L.add_argument("-RL", "--requirelower",   help="Password requires lowercase characters",action='store_true')
    parser_L.add_argument("-RU", "--requireupper",   help="Password requires uppercase characters",action='store_true')
    parser_L.add_argument("-RN", "--requirenumber",     help="Password requires numbers",action='store_true')
    parser_L.add_argument("-RS", "--requirespecial",help="Password requires special characters",action='store_true')
    group_L = parser_L.add_mutually_exclusive_group()
    group_L.add_argument("-w", "--word", help="Single word to convert to L33t Speak.",metavar='<word>')
    group_L.add_argument("-f", "--file", help="File to read in a list of words for conversion.",metavar='<file_path>')

    parser_L.set_defaults(func=convert_2_l33t)
#####
    parser_S = subparsers.add_parser('scram',formatter_class=argparse.RawTextHelpFormatter,help='The Scrambler:\n'
            '  This option will scramble provided words to every permutation, up to the number provided. \n'
            '  HINT 1: Every line in the provided file is 1 word, put each word on a new line.\n'
            '  HINT 2: When you select the # of words to concatenate, dont make it too high.\n'
            ' '
            )
    parser_S.add_argument("-n", "--num", help="Number of words to concatenate together\n"
            "(one line in file = one word) default:3",type=int,metavar='<number>',default=3)
    parser_S.add_argument("-f", "--file", help="File to read in a list of words for scrambling."
            ,required=True,metavar='<file_path>')
    parser_S.set_defaults(func=scramble_words)
#####
    parser_W = subparsers.add_parser('walker',formatter_class=argparse.RawTextHelpFormatter, help='The Walker:\n'
            '  This option will generate a keyboard walk password list.\n'
            '  HINT: Pay Attention to the LENGTH, do the math!\n'
            '  Set examples:\n'
            '   A = !QAZ,1qaz,@WSX,2wsx... all the way to the 5 key.\n'
            '   B = Same as above, but the whole keyboard.\n'
            '   C = !@,12,QW,qw,@#,23,WE,we... all the way to the 5 key. \n'
            '   D = 1qw2,!QW@,2we3,@WE#... all the way across the keyboard.\n'
            ' '
            )
    parser_W.add_argument("-s", "--set", help="Choice of keyboard walk sets:\n"
            "A = Sets of 4, 20 Elements, Vertical walk, Left Side, 1-5\n"
            "B = Sets of 4, 40 Elements, Vertical walk, Whole Keyboard\n"
            "C = Sets of 2, 64 Elements, Horizontal walk, Left Side, 1-5\n"
            "D = Sets of 4, 36 Elements, Loops on top, Whole Keyboard\n"
            ,choices=('A','B','C','D'),required=True)
    parser_W.add_argument("-l", "--length", help="Password length (MUST BE MULTIPLE OF 4, Default=12)",
            type=int,default=12,metavar='<number>')
    parser_W.set_defaults(func=walk_keyboard)
#####
    parser_G = subparsers.add_parser('gen',formatter_class=argparse.RawTextHelpFormatter,help='The Generator:\n'
            '  This option will generate a password list of your length and character set choosing.\n'
            '  Nothing like a good brute force attack!\n'
            ' '
            )
    parser_G.add_argument("-n", "--num", help="number of characters to make the password",required=True,type=int,metavar='<number>')
    parser_G.add_argument("-L", "--lowercase",   help="Use lowercase char set to generate passwords",action='store_true')
    parser_G.add_argument("-U", "--uppercase",   help="Use uppercase char set to generate passwords",action='store_true')
    parser_G.add_argument("-N", "--numbers",     help="Use numbers to generate passwords",action='store_true')
    parser_G.add_argument("-S", "--special",help="Use special characters to generate passwords",action='store_true')
    parser_G.add_argument("-H", "--hexchar",help="Use special characters to generate passwords",action='store_true')
    parser_G.add_argument("-RL", "--requirelower",   help="Password requires lowercase characters",action='store_true')
    parser_G.add_argument("-RU", "--requireupper",   help="Password requires uppercase characters",action='store_true')
    parser_G.add_argument("-RN", "--requirenumber",     help="Password requires numbers",action='store_true')
    parser_G.add_argument("-RS", "--requirespecial",help="Password requires special characters",action='store_true')
    parser_G.set_defaults(func=generate_words)

    args = parser.parse_args()
    args.func(args)
