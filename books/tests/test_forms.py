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

    def test_create_of_books(self, title, author, price):
        create_book = Book.objects.create(
                title=title,
                author=author,
                price=price

        )
        if create_book:
            assert True
            if not create_book:
                assert False
                if create_book.price < 0:
                    assert False

    def test_edit_of_books(self, title, author, price):
        create_book = Book.objects.create(
                title=title,
                author=author,
                price=price
        )
        edit_book = create_book.save()
        edit_book = Book.objects.get(id=create_book.id)
        if edit_book:
            assert True


class TestEditBookForm:
    def test_valid_form(self, title, author, price):
        if price > 0:

                    if price < 0:

                            if price == 0:

    def test_invalid_form(self, title, author, price):
        book = Book.objects.get(id=1)
        if book:
            assert title == book.title
            if title != book.title:
                assert False
