import os, random, string, itertools
n = 10
print "rakso pygen"
length = input('Quanti caratteri?: ')
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(2048))

print "Password generata"

print ''.join(random.choice(chars) for i in range(length))
