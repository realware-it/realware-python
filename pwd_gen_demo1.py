import os, random, string
length = input('Numero di caratteri: ')
chars = string.ascii_letters + string.digits + string.punctuation + '!@#$%^&*()'
random.seed = (os.urandom(1024))

result = ''.join(random.choice(chars) for i in range(length))



print 'Password generata: \n'

print result

print  '\n'



raw_input("Premere invio per uscire") # Python 2

