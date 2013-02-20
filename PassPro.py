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
	G = list()
	L = list('abcdefghijklmnopqrstuvwxyz')
	U = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	N = list('1234567890')
	S = list('~`!@#$%^&*()-_+=[]\{}|;:",./<>?')
			# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

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
		tempList = getattr(myArray, word[z])
		workingWord[z] = tempList[0]
		
	while finished != 86:

		tempChar = getattr(myArray, word[0])	#Pulls the current working value from the character array and assignes it to temp
		for i in range(length):					#Loops through leet characters of first element, (element0)
			workingWord[0] = tempChar[i]		#Assigns current character to word
			print("".join(workingWord))			#Displays current itteration of the word

		if endgame(workingWord, word) == 86:	#calls the function 'endgame' to find out if all itterations have been accomplished
			break						#breaks out of the while loop if all itterations have been accomplished

		element = 1					
		increment(word, workingWord, element)	#calls the 'increment' function to increment the rest of the elements

def file(fileName):
	with open(fileName, "r") as f:
		lines = f.read().splitlines()
	numLines = len(lines)
	for i in range(numLines):
		conversion(lines[i].lower())

def generator(num, options):
	tempList = []
	passLength = []
	print("num: ",num," options: ",options)
	for i in range(len(options)):
		tempList = tempList + getattr(myArray, options[i])
	setattr(myArray, 'G', tempList)

	for x in range(int(num)):
		passLength += "G"
	print("G-Unit",passLength)
	conversion(passLength)

		
def printTest(stuff):#~~~~~TESTING~~~~~
	print (stuff)	

def cliProcess(cliInput):
	for i in range(1, len(cliInput)):	#loops through the CLI peramaters
		
		if cliInput[i] == "-f":			#checks for File Input option
			file(cliInput[i+1])			#take the file name and passes it to the 'file' function
		
		elif cliInput[i] == "-g":
			print ("here?")
			generator(cliInput[i+1], cliInput[i+2])	#calls 'generator' function, passes NUMBER first, then OPTIONS

		elif cliInput[i] == "-w":				#checks for user input of a word
			conversion(cliInput[i+1].lower())	#passes the lowercase word to the 'conversion' function

	
	
#~~~~~~~~~~~PROGRAM STARTS HERE~~~~~~~~~~~	

myArray = arrays()
cliProcess(sys.argv)
