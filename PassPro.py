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
	L = list('abcdefghijklmnopqrstuvwxyz')
	U = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	N = list('1234567890')
	S = list('~`!@#$%^&*()-_+=[]\{}|;:",./<>?')

def endgame(workingWord, word):
	done = 0
	for i in range(len(workingWord)):		
		lastElement = getattr(arrays(), word[i])
		if workingWord[i] == lastElement[-1]:
			done += 1
			#print("NOPE")		#~~~TESTING~~~
		else:
			break
		if done == len(workingWord):
			finished = 86
			return finished

def increment(word, workingWord, element):
		
		tempChar = getattr(arrays(), word[element])				#Gets the list for the respective element in 'word'
		elementLength = len( getattr(arrays(), word[element]) )	#Gets the length of that list
		
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
	
	wordLength = len(word)			#determines the length of the inputed word
	workingWord = list(word)		#Takes each letter of the word and puts it in array
	finished = 0
	length = len (getattr(arrays(), word[0]) )	#gets length of characterset for first letter

	while finished != 86:

		tempChar = getattr(arrays(), word[0])	#Pulls the current working value from the character array and assignes it to temp
		for i in range(length):					#Loops through leet characters of first element, (element0)
			workingWord[0] = tempChar[i]		#Assigns current character to word
			print("".join(workingWord))			#Displays current itteration of the word

		if endgame(workingWord, word) == 86:	#calls the function 'endgame' to find out if all itterations have been accomplished
			break						#breaks out of the while loop if all itterations have been accomplished

		element = 1					
		increment(word, workingWord, element)	#calls the 'increment' function to increment the rest of the elements
	#return

def file(fileName):
	with open(fileName, "r") as f:
		lines = f.read().splitlines()
	
	numLines = len(lines)
	for i in range(numLines):
		conversion(lines[i])


def cliProcess(cliInput):
	for i in range(1, len(cliInput)):	#loops through the CLI peramaters
		
		if cliInput[i] == "-f":			#checks for File Input option
			file(cliInput[i+1])			#take the file name and passes it to the 'file' function
		
		elif cliInput[i] == "-w":
			conversion(cliInput[i+1])

	
	
#~~~~~~~~~~~PROGRAM STARTS HERE~~~~~~~~~~~	



cliProcess(sys.argv)#~~~~~TESTING~~~~~


#word = input('Input word: ')	#Input from User
#word = word.lower()				#Converts input to all Lowercase
#conversion (word)				#Calls the conversion function with the user inputed variable
#print("~~~~NEXT TRY~~~~")
#filename = "test.txt"		#~~~~~TESTING~~~~~
#file(filename)				#~~~~~TESTING~~~~~
		
 



#print sys.argv









"""
	num = 'a'
	num2 = 'b'

	z = getattr(arrays(), num)
	z2 = getattr(arrays(), num2)

	print (z)
	print (z2)

EXAMPLE STUFFs...

#"sqlimg%d" % var

for x in a:
	print(x)

#WORKS#
for i in range(len(word)):
	
	print(wordStart[i])

"""





