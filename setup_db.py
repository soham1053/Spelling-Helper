import sqlite3

conn = sqlite3.connect("database.sqlite")

c = conn.cursor()

c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username VARCHAR(128), password TEXT)")
# We should also create a word table

conn.commit()
conn.close()