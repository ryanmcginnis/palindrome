import re, os, time, string

def palindrome():
	try:
		os.system('clear')
		word = str(raw_input("give me a word\n")).lower() # remove case
		word = re.sub(r'\W+', '', word) # remove non-alphanumeric characters
		reversed = word[::-1] # reverse input
		if word.isalpha(): # is word all letters (after removing non-alpha)?
			os.system('clear')
			if reversed == word:
				print "This is a palindrome."
				time.sleep(0.5)
				palindrome()
			else:
				print "This is not a palindrome."
				time.sleep(0.5)
				palindrome()
		else:
			os.system('clear')
			print "Not a word."
			time.sleep(0.5)
			palindrome()
	except KeyboardInterrupt:
		os.system('clear')
		print "Quitting...\n"
		quit()
palindrome()
