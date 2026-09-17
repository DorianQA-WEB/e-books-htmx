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
