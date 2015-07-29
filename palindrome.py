import re, os, time

def palindrome():
	os.system('clear')
	word = raw_input("give me a word\n").lower() # remove case
	word = re.sub(r'\W+', '', word) # remove non-alphanumeric characters
	reversed = word[::-1] # reverse input
	os.system('clear')
	if reversed == word:
		print "This is a palindrome."
		time.sleep(0.5)
		palindrome()
	else:
		print "This is not a palindrome."
		time.sleep(0.5)
		palindrome()
palindrome()