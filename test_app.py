import unittest
import sqlite3
import ProgrammingTechnologyLAB2 as app

class TestLibraryApp(unittest.TestCase):
    def setUp(self):
        # Створення тестової бази даних
        self.conn = sqlite3.connect(':memory:')  
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            is_borrowed INTEGER
        )
        ''')
        self.conn.commit()

        # Перевизначення курсору та з'єднання в модулі
        app.conn = self.conn
        app.cursor = self.cursor

    def tearDown(self):
        self.conn.close()

    def test_add_book(self):
        # Перевірка успішного додавання книги
        result = app.add_book("Назва книги", "Автор книги")
        self.assertTrue(result)

        # Перевірка того, що книга була додана в базу
        self.cursor.execute('SELECT * FROM books WHERE title = ? AND author = ?', ("Назва книги", "Автор книги"))
        books = self.cursor.fetchall()
        self.assertEqual(len(books), 1)

    def test_add_book_empty(self):
        # Перевірка додавання книги з порожніми полями
        result = app.add_book("", "")
        self.assertFalse(result)

    def test_borrow_book(self):
        # Додавання книги
        app.add_book("Назва книги", "Автор книги")
        self.cursor.execute('SELECT id FROM books WHERE title = ?', ("Назва книги",))
        book_id = self.cursor.fetchone()[0]

        # Перевірка видачі книги
        result = app.borrow_book(book_id)
        self.assertTrue(result)

        # Перевірка статусу книги
        self.cursor.execute('SELECT is_borrowed FROM books WHERE id = ?', (book_id,))
        is_borrowed = self.cursor.fetchone()[0]
        self.assertEqual(is_borrowed, 1)

    def test_borrow_book_already_borrowed(self):
        # Додавання книги і її видача
        app.add_book("Назва книги", "Автор книги")
        self.cursor.execute('SELECT id FROM books WHERE title = ?', ("Назва книги",))
        book_id = self.cursor.fetchone()[0]
        app.borrow_book(book_id)

        # Спроба видати вже видану книгу
        result = app.borrow_book(book_id)
        self.assertFalse(result)

    def test_return_book(self):
        # Додавання книги і її видача
        app.add_book("Назва книги", "Автор книги")
        self.cursor.execute('SELECT id FROM books WHERE title = ?', ("Назва книги",))
        book_id = self.cursor.fetchone()[0]
        app.borrow_book(book_id)

        #Перевірка повернення книги
        result = app.return_book(book_id)
        self.assertTrue(result)

        # Перевірка статусу книги після повернення
        self.cursor.execute('SELECT is_borrowed FROM books WHERE id = ?', (book_id,))
        is_borrowed = self.cursor.fetchone()[0]
        self.assertEqual(is_borrowed, 0)

    def test_return_book_not_borrowed(self):
        #Перевірка додавання книги
        app.add_book("Назва книги", "Автор книги")
        self.cursor.execute('SELECT id FROM books WHERE title = ?', ("Назва книги",))
        book_id = self.cursor.fetchone()[0]

        # Спроба повернути книгу, яка не була видана
        result = app.return_book(book_id)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
