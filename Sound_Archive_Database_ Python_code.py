# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:16:40 2023

@author: lcavo
"""

import sqlite3 
conn=sqlite3.connect('SoundArchiveDatabase_Python.db') 
cursor=conn.cursor() 

cursor.execute('DROP TABLE IF EXISTS bl_data')
cursor.execute('CREATE TABLE bl_data (BL_Id INTEGER PRIMARY KEY, Composer TEXT, Composer_dates TEXT, Title TEXT, Pub_date_stand INTEGER, Pub_date_unstand INTEGER, Pub_place TEXT,Publisher TEXT)');
     
import csv 
          
with open('C:\\Users\\lcavo\\OneDrive\\Desktop\\GITHUB1_DATAMODELLING\\Sound_Archive_original_metadata_sample.csv', newline='', encoding="utf-8-sig") as csvfile:
         reader = csv.DictReader(csvfile)
         for row in reader:
                 cursor.execute('''INSERT INTO bl_data (BL_Id, Composer, Composer_dates, Title, Pub_date_stand, Pub_date_unstand, Pub_place, Publisher) 
                      VALUES (?,?,?,?,?,?,?,?)''',
                      (row["BL record ID"], row ["Composer"], row["Composer life dates"], row["Title"], row["Publication date (standardised)"], row["Publication date (not standardised)"], row["Place of publication"], row["Publisher"]))
    
cursor.execute('''SELECT * FROM bl_data''')

all_rows=cursor.fetchall()
print(all_rows) 


#Q1
cursor.execute('DROP TABLE IF EXISTS Composers')
cursor.execute('CREATE TABLE Composers (Composer_Id INTEGER PRIMARY KEY, Composer_Fname TEXT, Composer_Lname TEXT, Composer_Birth Integer, Composer_death INTEGER)');


#Q2
cursor.execute('''SELECT COUNT(DISTINCT Composer) FROM bl_data''') 
all_rows=cursor.fetchall()
print((all_rows))




#Q3
Composer='Aarons, Sam'
cursor.execute('''SELECT BL_Id FROM bl_data WHERE Composer=?''', (Composer,))

all_rows=cursor.fetchall()
print((all_rows))

#Q4

user_input=input('Select a city: ')
cursor.execute('''SELECT * FROM bl_data WHERE Pub_place=?''',(user_input,))

all_rows=cursor.fetchall()
print((all_rows))

#Q5 

user_input1=input('Select final letters: ')
cursor.execute('''SELECT * FROM bl_data WHERE Publisher LIKE?''',('%'+user_input1,))

all_rows=cursor.fetchall()
print((all_rows))

conn.commit()
conn.close()







