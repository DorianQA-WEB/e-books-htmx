import pytest
from django.utils import timezone
from books.forms import BookCreateForm, BookEditForm

class TestCreateBookForm:
    def test_valid_form(self, title, author, price):
        data = {
                'title': title,
                'author': author,
                'price': price
        }
        form = BookCreateForm(data=data)
        assert form.is_valid() == True

    def test_invalid_form(self, title, author, price):
        if price < 0:
            data = {
                    'title': title,
                    'author': author,
                    'price': price
                    }
            form = BookCreateForm(data=data)
            assert form.is_valid() == False

    def test_number_of_books(self, title, author, price):
        if len(Book.objects.all()) == 0:
                assert True


    def test_number_of_books(self, title, author, price):
        if len(Book.objects.all()) == 1:
                assert True
                if len(Book.objects.all()) > 1:
                    assert False