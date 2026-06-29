from django import forms

from .models import Book


class BookCreateForm(forms.ModelForm):
    title = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "disbtn",
                "placeholder": "Title",
            }
        ),
    )
    author = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={"class": "disbtn",
            "placeholder": "Author",
            }
        ),
    )
    price = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "disbtn",
                "placeholder": "Price",
            }
        ),
    )

    class Meta:
        model = Book
        fields = ["title", "author", "price"]