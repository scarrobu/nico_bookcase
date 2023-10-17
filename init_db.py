import sqlite3

# Create a database connection
conn = sqlite3.connect('knihy.db')
cursor = conn.cursor()

# Create a table to store reservations with a unique ID
cursor.execute('''
    CREATE TABLE IF NOT EXISTS reservations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT,
        book_title TEXT
    )
''')

# Close the database connection
conn.close()