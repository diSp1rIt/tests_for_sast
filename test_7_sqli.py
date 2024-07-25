import sqlite3
connection = sqlite3.connect('my_database.db')

cursor = connection.cursor()

a = input()

a += ' '

cursor.execute(F'SELECT * FROM{a[-1]}table')

connection.close()