# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!/usr/bin/python

import mysql
import random


# Open database connection
db = mysql.connect("localhost","root","r34lw4r3","infradb")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM utenti"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      nome = row[1]
      cognome = row[2]
      ip = row[3]
      ip_vpn = row[4]
      # Now print fetched result
      print "id=%s,nome=%s,cognome=%s,ip=%s,ip_vpn=%s" % \
             (id, nome, cognome, sex, income )
except:
   print "Errore: Impossibile trovare i dati richiesti"

# disconnect from server
db.close()