import sqlite3

# Connect to database
connection = sqlite3.connect("exam.db")

# cursor object that enables action on database
cursor = connection.cursor()

# Create database table
cursor.execute("CREATE TABLE IF NOT EXISTS students (name text, surname text, birthday integer)")

# Adding data to database
cursor.execute("INSERT INTO  students VALUES ('Yakup', 'Acar', '2007')")

# Commit action
connection.commit()

# Close commit
connection.close()
