import json
import sqlite3

# Connect to SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

# Create the posts table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    sub_title TEXT,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# Load JSON data
with open("posts.json", "r", encoding="utf-8") as file:
    posts = json.load(file)

# Insert posts into the database
for post in posts:
    cursor.execute(
        "INSERT INTO blog_post (title, sub_title, content, created_at) VALUES (?, ?, ?, datetime('now'))",
        (post["title"], post["sub_title"], post["content"])
    )

# Commit and close the connection
conn.commit()
conn.close()

print("✅ All posts have been added to the SQLite database successfully!")
