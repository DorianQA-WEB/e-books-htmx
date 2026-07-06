# напиши док стринги

# models.py
from django.db import models


class Book(models.Model):
    """
    Модель, представляющая книгу в библиотеке.

    Атрибуты:
        title (str): Название книги (максимум 200 символов). Может быть пустым.
        author (str): Имя автора книги (максимум 200 символов). Может быть пустым.
        price (int): Цена книги в целых единицах. Допускает только неотрицательные значения.
                     Может быть NULL в БД.
        read (bool): Флаг, указывающий, прочитана ли книга. По умолчанию `False`.

    Методы:
        __str__(): Возвращает строковое представление книги — её название.
    """
    title = models.CharField(
        max_length=200,
        blank=True
    )
    author = models.CharField(
        max_length=200,
        blank=True
    )
    price = models.PositiveIntegerField(
        blank=True,
        null=True
    )
    read = models.BooleanField(
        default=False,
        blank=True
    )

    def __str__(self):
        """
        Возвращает строковое представление объекта книги.

        Используется в админке, формах и шаблонах при отображении объекта.
        Возвращает только название книги, так как оно обычно уникально и информативно.

        Returns:
            str: Название книги (значение поля `title`).
        """
        return self.title
