# read_from_social_media_db.py

# Connect the database to Python using the sqlite3 module
import sqlite3

# Create a connection to the database
conn = sqlite3.connect("sm_app.sqlite")

# Create a cursor
cursor = conn.cursor()

# Create a SELECTION command
select_posts = """
SELECT title, description
FROM posts
"""

# Fetch all posts
posts = cursor.execute(select_posts).fetchall()

# Close the connection
conn.close()
