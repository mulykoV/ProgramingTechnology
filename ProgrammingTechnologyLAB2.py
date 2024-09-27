import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# Створення таблиці для книг
def initialize_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        is_borrowed INTEGER
    )
    ''')
    conn.commit()

# Функція для додавання книги
def add_book(title, author):
    if title and author:
        cursor.execute('INSERT INTO books (title, author, is_borrowed) VALUES (?, ?, ?)', (title, author, 0))
        conn.commit()
        return True
    return False

# Функція для отримання списку книг
def get_books():
    cursor.execute('SELECT * FROM books')
    return cursor.fetchall()

# Функція для видачі книги
def borrow_book(book_id):
    cursor.execute('UPDATE books SET is_borrowed = 1 WHERE id = ? AND is_borrowed = 0', (book_id,))
    if cursor.rowcount > 0:
        conn.commit()
        return True
    return False

# Функція для повернення книги
def return_book(book_id):
    cursor.execute('UPDATE books SET is_borrowed = 0 WHERE id = ? AND is_borrowed = 1', (book_id,))
    if cursor.rowcount > 0:
        conn.commit()
        return True
    return False
