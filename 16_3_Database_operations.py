import sqlite3

# Creating Database
connection = sqlite3.connect("school.db")

# Create cursor
cursor = connection.cursor()

# Creating table
cursor.execute("""CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    grade INTEGER,
    branch TEXT,
    birthday TEXT, 
    notes TEXT
)""")

while True:
    answer = input("""please select the action to do:
    1. Add student
    2. Edit student
    0. Exit
    """)
    if answer == "0":
        break
    if answer == "1":
        name = input("Student's name: ")
        surname = input("Student's surname: ")
        grade = int(input("Student's grade: "))
        branch = input("Student's branch: ")
        birthday = input("Student's birthday (dd.mm.yy): ")
        notes = input("Student's notes (comma separated): ")

        cursor.execute(f" "
                       f"INSERT INTO students (name, surname, grade, branch, birthday, notes) "
                       f"VALUES('{name}', '{surname}', {grade}, '{branch}', '{birthday}', '{notes}')")
        connection.commit()
    elif answer == "2":
        name = input("enter name of the student to edit:")
        notes = input("Student's new notes (comma separated): ")

        cursor.execute(f"UPDATE students  SET notes = '{notes}' WHERE name = '{name}'")
        connection.commit()

connection.commit()
connection.close()
