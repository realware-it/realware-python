# Attende sino a quando non viene inserita la giusta password. 
# Usate Control-C per fermare il programma senza password.

# Notate che se non viene inserita la giusta password, il ciclo 
# while prosegue all'infinito.
password = "aaa"

# Notate il simbolo != (diverso).
while password != "palle":
    password = raw_input("Password:")
print "Welcome in"