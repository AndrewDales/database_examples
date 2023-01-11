# Connect the database to Python using the sqlite3 module
import sqlite3

# Create a connection to the database
conn = sqlite3.connect("student.sqlite")

# Create a cursor
cursor = conn.cursor()

# Create a SELECTION command
select_students = """
SELECT id, firstname, lastname
FROM students
WHERE age >= 15
"""

# Choose how many students to fetch - note that each fetch statement fetches data from
# the point where it has previously been fetched
cursor.execute(select_students)
first_student = cursor.fetchone()
more_students = cursor.fetchmany(10)
other_students = cursor.fetchall()

# Aggregate query
average_query = """
SELECT avg(age)
FROM students
WHERE gender = ?
"""
average_age = cursor.execute(average_query, ('female',)).fetchone()[0]

conn.close()
