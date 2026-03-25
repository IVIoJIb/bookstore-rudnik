import unittest
from models import Book

class TestBookModel(unittest.TestCase):
    def test_book_creation(self):
        # Перевіряємо, чи правильно створюється об'єкт
        book = Book("Kobzar", "Taras Shevchenko", 500)
        self.assertEqual(book.title, "Kobzar")
        self.assertEqual(book.price, 500)
