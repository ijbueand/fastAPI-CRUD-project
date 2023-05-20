import sqlite3
import csv

con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS my_table (ID TEXT, Name TEXT, email TEXT, Role TEXT, Group_name TEXT)')

with open('datos_alumnos.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        cur.execute('INSERT INTO my_table (ID, Name, email, Role, Group_name) VALUES (?, ?, ?, ?, ?)', row)

con.commit()
con.close()

print("La base de datos se ha poblado correctamente.")