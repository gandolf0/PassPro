PassPro
=======

PassPro is a password generation tool that allows you to create custom wordlists to be used with password cracking or spraying. The script has 4 functions listed below.

# PassPro Functions:
## The L33t Converter
This option will convert provided words to every permutation of leet speak.
```
python passpro.py leet -h
usage: PassPro leet [-h] [-m <2022,123!>] [-w <word> | -f <file_path>]

options:
  -h, --help            show this help message and exit
  -m <2022,123!>, --mangle <2022,123!>
                        Add a manglinger to the end of the password.(Comma seperated)
  -w <word>, --word <word>
                        Single word to convert to L33t Speak.
  -f <file_path>, --file <file_path>
                        File to read in a list of words for conversion.
```

## The Scrambler
This option will scramble provided words to every permutation, up to the number provided.
    HINT 1: Every line in the provided file is 1 word, put each word on a new line.
    HINT 2: When you select the # of words to concatenate, dont make it too high.
```
python passpro.py scram -h
usage: PassPro scram [-h] [-n <number>] -f <file_path>

options:
  -h, --help            show this help message and exit
  -n <number>, --num <number>
                        Number of words to concatenate together
                        (one line in file = one word) default:3
  -f <file_path>, --file <file_path>
                        File to read in a list of words for scrambling.
```
    
## The Walker:
This option will generate a keyboard walk password list.
    HINT: Pay Attention to the LENGTH, do the math!
    Set examples:
        A = !QAZ,1qaz,@WSX,2wsx... all the way to the 5 key.
        B = Same as above, but the whole keyboard.
        C = !@,12,QW,qw,@#,23,WE,we... all the way to the 5 key.
        D = 1qw2,!QW@,2we3,@WE#... all the way across the keyboard.
```
python passpro.py walker -h
usage: PassPro walker [-h] -s {A,B,C,D} [-l <number>]

options:
  -h, --help            show this help message and exit
  -s {A,B,C,D}, --set {A,B,C,D}
                        Choice of keyboard walk sets:
                        A = Sets of 4, 20 Elements, Vertical walk, Left Side, 1-5
                        B = Sets of 4, 40 Elements, Vertical walk, Whole Keyboard
                        C = Sets of 2, 64 Elements, Horizontal walk, Left Side, 1-5
                        D = Sets of 4, 36 Elements, Loops on top, Whole Keyboard
  -l <number>, --length <number>
                        Password length (MUST BE MULTIPLE OF 4, Default=12)
```

## The Generator
This option will generate a password list of your length and character set choosing.
Nothing like a good brute force attack!
```
python passpro.py gen -h
usage: PassPro gen [-h] -n <number> [-L] [-U] [-N] [-S]

options:
  -h, --help            show this help message and exit
  -n <number>, --num <number>
                        number of characters to make the password
  -L, --lowercase       Use lowercase char set to generate passwords
  -U, --uppercase       Use uppercase char set to generate passwords
  -N, --numbers         Use numbers to generate passwords
  -S, --special         Use special characters to generate passwords
```

### passpro.py help
```
python passpro.py -h
usage: PassPro [-h] [-o <file_path>] {leet,scram,walker,gen} ...

positional arguments:
  {leet,scram,walker,gen}
                        Features of Password Producer|Professional:
    leet                The L33t Converter:
                          This option will convert provided words to every permutation of leet speak.

    scram               The Scrambler:
                          This option will scramble provided words to every permutation, up to the number provided.
                          HINT 1: Every line in the provided file is 1 word, put each word on a new line.
                          HINT 2: When you select the # of words to concatenate, dont make it too high.

    walker              The Walker:
                          This option will generate a keyboard walk password list.
                          HINT: Pay Attention to the LENGTH, do the math!
                          Set examples:
                           A = !QAZ,1qaz,@WSX,2wsx... all the way to the 5 key.
                           B = Same as above, but the whole keyboard.
                           C = !@,12,QW,qw,@#,23,WE,we... all the way to the 5 key.
                           D = 1qw2,!QW@,2we3,@WE#... all the way across the keyboard.

    gen                 The Generator:
                          This option will generate a password list of your length and character set choosing.
                          Nothing like a good brute force attack!


options:
  -h, --help            show this help message and exit
  -o <file_path>, --output <file_path>
                        File to save results to.
```
