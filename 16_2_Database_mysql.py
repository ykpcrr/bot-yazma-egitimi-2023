import mysql.connector
from settings import *

# Connect MySQL database
connection = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)

# Cursor object that enables action on database
cursor = connection.cursor()

# Create table on database
cursor.execute("CREATE TABLE IF NOT EXISTS students (name CHAR(30), surname CHAR(25), birthday SMALLINT)")

# Adding data to database
sql = "INSERT INTO students (name, surname, birthday) VALUES (%s, %s, %s)"
params = ("Yakup", "surname", "1999")
cursor.execute(sql, params)

# Commit actions
connection.commit()

# Close connection
connection.close()
