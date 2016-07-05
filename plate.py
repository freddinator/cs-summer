import re

numberplate = input("Enter numberplate > ")
numberplate = numberplate.replace(" ", "")

re1='([a-z])'	# Any character
re2='([a-z])'
re3='(\\d)'	    # Any digit
re4='(\\d)'	    # Any digit
re5='([a-z])'	
re6='([a-z])'
re7='([a-z])'

rg = re.compile(re1+re2+re3+re4+re5+re6+re7,re.IGNORECASE|re.DOTALL)

if rg.match(numberplate) and len(numberplate) == 7:
	print ("\033[92m ✔ Valid\033[0m")
else:
	print ("\033[91m ✗ Invalid\033[0m")