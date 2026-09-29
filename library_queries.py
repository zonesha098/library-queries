import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create books table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    book_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    genre TEXT NOT NULL,
    price REAL NOT NULL,
    stock INTEGER NOT NULL
)
""")

# Insert 8 sample books
books = [
    (1, "The Great Gatsby", "Fiction", 1200, 8),
    (2, "To Kill a Mockingbird", "Fiction", 950, 3),
    (3, "1984", "Fiction", 1500, 2),
    (4, "Python Programming", "Technology", 2200, 6),
    (5, "Data Science Basics", "Technology", 1800, 4),
    (6, "The Alchemist", "Fiction", 1100, 7),
    (7, "Clean Code", "Technology", 2500, 3),
    (8, "Harry Potter", "Fantasy", 1300, 10)
]

cursor.executemany("""
INSERT OR IGNORE INTO books
(book_id, title, genre, price, stock)
VALUES (?, ?, ?, ?, ?)
""", books)

conn.commit()

# (a) Price > 1000, sorted descending
print("\n(a) Books with price > 1000, sorted by price descending:")

cursor.execute("""
SELECT title, price
FROM books
WHERE price > 1000
ORDER BY price DESC
""")

for row in cursor.fetchall():
    print(row)

# (b) Rename title as book_title
print("\n(b) Title renamed using AS:")

cursor.execute("""
SELECT title AS book_title, price
FROM books
""")

for row in cursor.fetchall():
    print(row)

# (c) Fiction books with stock < 5
print("\n(c) Fiction books with stock < 5:")

cursor.execute("""
SELECT *
FROM books
WHERE genre = 'Fiction'
AND stock < 5
""")

for row in cursor.fetchall():
    print(row)

conn.close()