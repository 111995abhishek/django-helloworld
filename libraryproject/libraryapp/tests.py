from django.test import TestCase
from libraryapp.models import Book,Author


class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(book_name="machine learning",price=500,available=True,Isbn=45467)

        # Book.objects.create(book_name="head first python",stock=700)
    def test_case(self):
        ml = Book.objects.get(book_name="machine learning")
        # head_first_python = Book.objects.get(Book_name="head first python")
        self.assertEqual(ml.get_b_name(), "machine learning")
        # self.assertEqual(Book_name= head first_python)


