#!/usr/bin/python

import mysql.connector
import tablib
import sys
import random
import xtopdf

# Open database connection
db = mysql.connector.connect(user='root',password='r34lw4r3',host='192.168.2.73',port='3306',database='infradb')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.



cursor.execute ("select id, usr_status, usr_pc from users")
   
   
# fetch all of the rows from the query
data = cursor.fetchall ()



# Questo sarà l'elenco delle intestazioni. Deve avere tanti elementi quante sono le colonne estratte dalla select sul DB.
headers = ['id', 'usr_status', 'usr_pc', 'usr_ip', 'usr_ip_vpn'];

# Questo è l'array con le dimensioni di ogni colonna. Anche questo deve avere tanti elementi quante sono le colonne estratte dalla select sul DB.
widths = [5, 12, 8, 8, 12]

# Il separator è calcolato in base alla larghezza delle colonne.
separator = '-' * sum(widths)

# Inizializiamo il PDF con nome del file e tipo di carattere.
pw = PDFWriter('export.pdf')
pw.setFont('Courier', 10)

# Impostazione dell'header e del footer.
pw.setHeader('Testo per per l\'header')
pw.setFooter('Testo per il footer')

# Scrittura delle intestazioni delle colonne nel PDF.
print_and_write(pw, separator)
print_and_write(pw, ''.join([ header.center(widths[idx]) for idx, header in enumerate(headers) ]))
print_and_write(pw, separator)

# Scrittura delle righe dei risultati nel PDF
for row in data :
	print_and_write(pw, ''.join([ str(val).center(widths[idx]) for idx, val in enumerate(row) ]))

# Chiusura del PDF.
print_and_write(pw, separator)
pw.close()
