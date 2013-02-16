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
	#abc = list('abcdefghijklmnopqrstuvwxyz')
	#ABC = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
	#123 = list('1234567890')
	#spl = list('~`!@#$%^&*()-_+=')
	
"""
	num = 'a'
	num2 = 'b'

	z = getattr(arrays(), num)
	z2 = getattr(arrays(), num2)

	print (z)
	print (z2)
"""


word = input('Input word: ')	#Input from User

word = word.lower()				#Converts input to all Lowercase

wordLength = len(word)

workingWord = list(word)		#Takes each letter of the word and puts it in array

print("\nstarting word:", word)	#~~~TESTING~~~

element=0
length = len (getattr(arrays(), word[element]) )	#gets length of characterset for first letter
print ("length", length)	#~~~TESTING~~~
print("\nTest...\n")		#~~~TESTING~~~

tempChar = getattr(arrays(), word[element])	#Pulls the current working value from the character array and assignes it to temp
for i in range(length):					#Loops through leet characters of first element
	workingWord[element] = tempChar[i]		#Assigns current character to word
	print("\nWord: ", "".join(workingWord))	#Displays current itteration of the word


element += 1	
tempChar = getattr(arrays(), word[element])
elementLength = len( getattr(arrays(), word[element]) )

if workingWord[element] != tempChar[-1]:		#checks to see if second element is at the end
	
	for z in range(elementLength):
		if workingWord[element] == tempChar[z]:
			workingWord[element] = tempChar[z+1]
			break
		
	#gets confusing...
elif workingWord[element] == tempChar[-1]:		#if element is at the end of array
	
	for x in range(elementLength):				#start looping through that element
	
		if workingWord[element] == tempChar[-1]:	#checks if element is at the end
		
			if x != wordLength:
				workingWord[element] == tempChar[0]						#set second element back to start
				
			element += 1	
			elementLength = len( getattr(arrays(), word[element]) )	#grab value from next element over
			tempChar2 = getattr(arrays(), word[element])
	
			for y in range(elementLength):
				
				if workingWord[element] == tempChar2[y] and workingWord[element] != tempChar2[-1]:
					
					workingWord[element] == tempChar[y+1]
					if workingWord[element] == tempChar2[-1]:
						break
					break


	
print("\nWord: ", "".join(workingWord))
			
"""	

class endgame:
	done = 0
	for i in range(len(workingWord)):		
		lastElement = getattr(arrays(), word[i])
		if workingWord[i] == lastElement[-1]:
			done += 1
		#else BREAK
		#if done == len(workingWord)
#program finished
	

class cycle:
	
	tempChar = getattr(arrays(), word[a])	#Pulls the current working value from the character array and assignes it to temp
	
	for i in range(length):		#Loops through leet characters of first element
		workingWord[a] = tempChar[i]		#Assigns current character to word
		print("\nWorking Word: ", "".join(workingWord))
		#print("word:" + str(workingWord))	#Prints the output with out the crap around the list, that is what .join is for
		print("WOrking word output:" + str(workingWord))


EXAMPLE STUFFs...

#"sqlimg%d" % var

for x in a:
	print(x)

#WORKS#
for i in range(len(word)):
	
	print(wordStart[i])

	
	
	
how do i print something in python with out all the formating crap?
statement~~~~~: print ('Working word output: ', workingWord)
actual output~~~: Working word output: ['a', 's']
desired output~: Working word output: as
i don't want all the brackets, quotes or commas
"""









"""
sub leetPass{	#Option 1 Menu/CLI
	#open(File, '>>', "Variants.txt");#Opens file
	

	for ($pswrd=0; $pswrd <= $#passwords; $pswrd++){
		if ($input == 2) {						#Checks if the input is from a file
			$myPass = lc(@passwords[$pswrd]);	#Moves current password from file into $myPass varable and ensures it's lowercase
		}# else { $#passwords = 0;} 
		
		@leetPass = ();					#Zeros out leetPass array before starts with new word
		@pass = split(//, $myPass);		#Parses individual characters of input and puts them into array elements
		#print "pass array: @pass\n\n";
		for ($p=0; $p <= $#pass; $p++) {
			$temp = @pass[$p];				#Converts the incremented letter of the user input into a string
			@char = @$temp;					#Uses that string to assign the corresponding array
			@leetPass[$p] = @char[0];   	###Populates @leetPass with the starting variables
		}
		#FYI Info:
		# @pass 	= lowercase input from user
		# @leetPass = working modified password 

		#finds the END/LAST variable to end program
		$tempA = @pass[-1];				#Converts last letter of the user input into a string
		@veryLast = @$tempA;			#Uses that string to assign the corresponding array
		
		$finish = 0;
		#loops until all possibilities have been cycled through
		while ($finish != 86) {
			$tempB = @pass[0];					#Converts first letter of the user input into a string
			@first = @$tempB;					#Uses that string to assign the corresponding array

			for ($t=0; $t <= $#first; $t++) {	#Loops first element through all letters
				$leetPass[0] = @first[$t];		#Inputs the letter into that element
				#print (File @leetPass, "\n");	#Outputs possible password to the Variant.txt file
				print @leetPass, "\n";			#Used to display output on screen
			}
			
			#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			# \/~~DETERMINE IF ALL POSSIBILITIES HAVE BEEN USED~~\/
			$done = 0;	
			for ($w=0; $w <= $#pass; $w++) {				#Loops through all elements of @leetPass array
				$tempC = @pass[$w];							#Converts incremented letter of the user input into a string
				@element = @$tempC;							#Uses that string to assign the corresponding array
				#if element in question is at the end, increment $done
				if ($leetPass[$w] eq @element[-1]) {$done++;}
				#if every element is at the end then trigger the finish
				if ($done == $#pass+1) { $finish = 86; }
			}
			# /\~~DETERMINE IF ALL POSSIBILITIES HAVE BEEN USED~~/\
			#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
			
			$tempC = @pass[1]; 			#Converts second letter of the user input into a string
			@last = @$tempC;			#Uses that string to assign the corresponding array
			$z=1;
			#If element n question is not at the end
			if ($leetPass[$z] ne @last[-1]) {
				for ($i=0; $i <= $#last; $i++) { 		# Loop for finding what char is currently in element
					if ($leetPass[$z] eq @last[$i]) {	# Finds char thats currently in element
						$leetPass[$z] = @last[$i+1];	# Assigns value of next char to that element
						$i=$#last+1;					# Ends the for loop
					}
				}
			#If element n question is at the end
			} elsif ($leetPass[$z] eq @last[-1]) {

				for ($s=1; $s <= $#pass; $s++) {	#Loop through all possibilities in that element

						#If element n question is at the end of that array
					if ($leetPass[$s] eq @last[-1]) { 
						
						#If element index($s) is not equal to last element index 
						if ($s != $#pass) {
							$leetPass[$s] = @last[0];	#resets the second element back to start value
						}	
						
						$working = $s+1;				#Starts the working element at  
						$tempD = @pass[$working]; 		#Converts incremented letter of the user input into a string
						@last = @$tempD;				#Uses that string to assign the corresponding array
					
						for ($y=0; $y <= $#last; $y++) {#Loops element through all letters
						
							#If element in question equals current array value
							# &&
							#Element in question doesn't equal last vlaue in array
							if (($leetPass[$working] eq @last[$y]) && ($leetPass[$working] ne @last[-1])) {
								
								$leetPass[$working] = @last[$y+1];		#Inputs next elements value into leetPass
								$y=$#last+1;							#Ends loop
								#If next element is at end; exit exterior loop
								if ($leetPass[$working] eq @last[-1]) { $s = $#pass +1; }
							}
						}
					
					} else { $s = $#pass+1; } # this does something important, I forget what :-P
					#increments $working as long as its not past the length of the inputted password
					if ($working <= $#leetPass) {$working++;}
				}
			}
		}
	}#end for
	if ($input == 2) {close(dict);}
	#close(File);		#Closes file

"""
