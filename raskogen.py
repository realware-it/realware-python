import os, random, string, Tkinter
length = input('Numero di caratteri: ')
import tkMessageBox
n=length
if length < 12:
	    print "Password  debole\n"
	
else:
    print "Password abbastanza cazzuta\n"
	
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))
result = ''.join(random.choice(chars) for i in range(length)) 
print ("#") * 50
print "\n"
print result
print "\n"
print ("#") * 50
raw_input("Premere invio per uscire") # Python 2


