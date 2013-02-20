import sys
class arrays:
	a = list('aA@4')
	b = list('bB8')
	c = list('cC(')
	d = list('dD')
	e = list('eE3')
	f = list('fF')
	g = list('gG9')
	h = list('hH')
	i = list('iI!1')
	j = list('jJ')
	k = list('kKx')
	l = list('lL!1')
	m = list('mM')
	n = list('nN')
	o = list('oO0')
	p = list('pP')
	q = list('qQ')
	r = list('rR')
	s = list('sS$')
	t = list('tT!+7')
	u = list('uU')
	v = list('vV')
	w = list('wW')
	x = list('xX')
	y = list('yY')
	z = list('zZ')
	K = list()	#blank for filling later(kustom variables)
	G = list()	#blank for combining variables for the generator function
	L = list('abcdefghijklmnopqrstuvwxyz')
	U = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	N = list('1234567890')
	S = list('~`!@#$%^&*()-_+=[]\{}|;:",./<>?')
			# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
			
		#Sets of 4, 24 Elements, Left Side ONLY	
	A = ["!QAZ","1qaz","ZAQ!","zaq1","\@WSX","2wsx","XSW@","xsw2","#EDC","3edc","CDE#","cde3","\$RFV","4rfv","VFR\$","vfr4","%TGB","5tgb","BGT%","bgt5","^YHN","6yhn","NHY^","nhy6"]
		#Set of 2, 64 Elements, Left & Right, Left Side ONLY
	B = ["!\@","\@!","QW","WQ","AS","SA","ZX","XZ","12","21","qw","wq","as","sa","zx","xz","@#","#@","WE","EW","SD","DS","XC","CX","23","32","we","ew","sd","ds","xc","cx","#\$","\$#","ER","RE","DF","FD","CV","VC","34","43","er","re","df","fd","cv","vc","\$%","%\$","RT","TR","FG","GF","VB","BV","45","54","rt","tr","fg","gf","vb","bv"]
		#Set of 4, 32 Elements, Whole Keyboard
	C = ["!QAZ","1qaz","ZAQ!","zaq1","\@WSX","2wsx","XSW\@","xsw2","#EDC","3edc","CDE#","cde3","\$RFV","4rfv","VFR\$","vfr4","%TGB","5tgb","BGT%","bgt5","^YHN","6yhn","NHY^","nhy6","&UJM","mju7","*IK<",",ki8","(OL>",".lo9",")P:?","/;p0"]
		#Set of 4, 20 Elements, Loops on top, Left Side
	D = ["!QW\@","\@WQ!","1qw2","2wq1","\@WE#","#EW\@","2we3","3ew2","#ER\$","\$RE#","3er4","4re3","\$RT%","%TR\$","4rt5","5tr4","%TY^","^YT%","5ty6","6yt5"]

def endgame(workingWord, word):
	done = 0
	for i in range(len(workingWord)):		
		lastElement = getattr(myArray, word[i])
		if workingWord[i] == lastElement[-1]:
			done += 1
		else:
			break
		if done == len(workingWord):
			finished = 86
			return finished

def increment(word, workingWord, element):
		
		tempChar = getattr(myArray, word[element])				#Gets the list for the respective element in 'word'
		elementLength = len( getattr(myArray, word[element]) )	#Gets the length of that list
		
		if workingWord[element] != tempChar[-1]:			#checks if element in workingWord IS NOT at the end
			
			for z in range(elementLength):					#loops through that element
				if workingWord[element] == tempChar[z]:		#finds the matching character from the respective list
					workingWord[element] = tempChar[z+1]	#assignes the next character in that list to 'workingWord'
					break		#breaks out of the for loop

		elif workingWord[element] == tempChar[-1]:	#checks if element in workingWord IS at the end
			
			workingWord[element] = tempChar[0]		#resets the current element in 'workingWord' back to start value
			element +=1								#increments the element value
			increment(word, workingWord, element)	#calls another itteration of the 'increment' function with the updated variables

		return workingWord

def conversion(word):
	workingWord = list(word)		#Takes each letter of the word and puts it in array
	finished = 0
	length = len (getattr(myArray, word[0]) )	#gets length of characterset for first letter
	
	for z in range(len(word)):					#loop for initilazing the variables
		tempList = getattr(myArray, word[z])	#takes the respective list and assignes that to a temp variable
		workingWord[z] = tempList[0]			#take the first char of that list and assignes it to the respective element in the working word
		
	while finished != 86:

		tempChar = getattr(myArray, word[0])	#Pulls the current working value from the character array and assignes it to temp
		for i in range(length):					#Loops through leet characters of first element, (element0)
			workingWord[0] = tempChar[i]		#Assigns current character to word
			print("".join(workingWord))			#Displays current itteration of the word

		if endgame(workingWord, word) == 86:	#calls the function 'endgame' to find out if all itterations have been accomplished
			break						#breaks out of the while loop if all itterations have been accomplished

		element = 1					
		increment(word, workingWord, element)	#calls the 'increment' function to increment the rest of the elements

def file(fileName):								#input from a file for leet conversion
	with open(fileName, "r") as f:				#opens the file 
		lines = f.read().splitlines()			#assignes each line of text to an element in 'lines'
	numLines = len(lines)
	for i in range(numLines):					#cycles through each element/line of text 
		conversion(lines[i].lower())			#runs it through the leet converter

def generator(num, options):					#brute force type generator
	tempList = []
	passLength = []
	for i in range(len(options)):				#cycles through the options requested from user
		tempList += getattr(myArray, options[i])#combines those options to 1 temp list
	setattr(myArray, 'G', tempList)				#assignes that to the 'G' list in the arrays() class above

	for x in range(int(num)):					#cycles through the number of characters you want generated
		passLength += "G"						#adds a 'G' to the password length variable every pass
	conversion(passLength)						#passes that to the converson function to cycle through 

def walker(num, charSet):
	passLength = []
	for x in range(int(num)):
		passLength += charSet
	conversion(passLength)
	
def custom(num, fileName):
	passLength = []
	with open(fileName, "r") as f:
		lines = f.read().splitlines()
	setattr(myArray, 'K', lines)
	
	for x in range(int(num)):
		passLength += 'K'

	conversion(passLength)	

def cliProcess(cliInput):
	for i in range(1, len(cliInput)):	#loops through the CLI peramaters
		
		if cliInput[i] == "-f":			#checks for File Input option (-f <fileName>)
			file(cliInput[i+1])			#take the file name and passes it to the 'file' function
		
		elif cliInput[i] == "-g":		#checks for brute force option (-g ## <options>
			generator(cliInput[i+1], cliInput[i+2])	#calls 'generator' function, passes NUMBER first, then OPTIONS
		
		elif cliInput[i] == "-k":		#checks for keyboard walk option (-k ## <characterSet>)
			walker(cliInput[i+1], cliInput[i+2])
			
		elif cliInput[i] == "-c":		#check for file with custom variables (-c ## <filename>)
			custom(cliInput[i+1], cliInput[i+2])
		
		elif cliInput[i] == "-w":				#checks for user input of a word
			conversion(cliInput[i+1].lower())	#passes the lowercase word to the 'conversion' function
		
		else:
			help()
			
def help():
	SHIT = '''
NAME
  Password Pro

DESCRIPTION
  Put stuff here

OPTIONS
  
	(Leet Converter) 
	-w <word> ~~OR~~ -f <filename> IE:(-w password) ~~OR~~ (-f passwords.txt)
  
	This will convert a password into every variant	of leet 
	speak. You have 2 options for input, by file or by one word 
	at a time... (f)-file input, (w)-user input. 
	
	(The Generator)
	-g ## <LUNS> IE:(-g 2 LNS)
  
	This will output every possable varriant of Lowercase, 
	Uppercase, Numbers and Special Caracters to the length 
	you specify. To activate the characters, use the 
	following: (L)-Lowercase, (U)-Uppercase, (N)-Numbers and 
	(S)-Special Caracters

	(The Scrambler)
	-s ## <filename> IE:(-s 2 options.txt)
  
	This works if you know what is in the password but dont know 
	the order it goes in. This will rearrange the parts you give 
	it into every possable outcome. You first specify the number 
	of variables you want to use in a row, then you give it	the 
	file these variables exist in. Lets say you have 2 different 
	parts to your password and you know the first part could be 
	1 of 6 options and the second part could be 1 of 2 options. 
	You would put all 8 options in a file and specify 2	
	variables:(-s-2-options.txt) This will give you every possable
	arangement of your options. This program will also add a NULL
	value into the list of options for good measure.

	
	(Keyboard Walker)
	-k # A IE:(-k 1 A) A is character set, 3 is # of times used
  
	This will generate keyboard patterns based on different
	character sets. The example used above uses character set
	1, 3 times. Since character set 1 has 4 letters in each 
	set the password length will be the 3 times the length of
	the set, 12. There will be some excess passwords that will 
	most likely never be used but they are added due to the 
	programing and to ensure every possability is used.
	'''
	print(SHIT)	
#~~~~~~~~~~~PROGRAM STARTS HERE~~~~~~~~~~~	

myArray = arrays()
cliProcess(sys.argv)







