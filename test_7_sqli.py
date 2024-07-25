import sqlite3
connection = sqlite3.connect('my_database.db')

cursor = connection.cursor()

a = input()

a += ' '

# t = a
# a = a.split()
# a.append(t)

cursor.execute(F'SELECT * FROM{a[-1]}table')

connection.close()