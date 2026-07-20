from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from django.views.decorators.http import require_http_methods
from django.utils.translation import gettext_lazy as _
from .forms import BookCreateForm, BookEditForm
from .models import Book
from django.core.cache import cache


@require_http_methods(['GET'])
def book_list(request):
    """
    Обрабатывает GET-запрос на отображение списка всех книг и главной страницы.

    Возвращает страницу `base.html` с полным списком книг, формой создания книги
    (без автогенерированных ID полей) и контекстом для рендеринга.

    Args:
        request (HttpRequest): Объект HTTP-запроса.

    Returns:
        HttpResponse: Отображает шаблон `base.html` со списком книг и формой.
    """
    book_list = cache.get('cached_book_list')
    if not book_list:
        book_list = Book.objects.all()
        cache.set('cached_book_list', book_list,)
    form = BookCreateForm(auto_id=False)
    return render(
        request,
        'base.html',
        {'book_list': book_list, 'form': form}
    )

@require_http_methods(['POST'])
def create_book(request):
    """
    Обрабатывает POST-запрос на создание новой книги.

    Принимает данные из формы, валидирует и сохраняет в БД.
    Возвращает фрагмент `partial_book_detail.html` — отдельную строку таблицы
    только что созданной книги (для подстановки через htmx).

    Args:
        request (HttpRequest): Объект HTTP-запроса с POST-данными.

    Returns:
        HttpResponse: Рендерит `partial_book_detail.html` с созданной книгой.
                      В случае невалидной формы — отрендерит с ошибкой (но ошибка
                      не обрабатывается, см. замечание ниже).
    """
    form = BookCreateForm(request.POST)
    if form.is_valid():
        book = form.save()
    return render(request,
                  'partial_book_detail.html',
                  {'book': book})

def update_book_details(request, pk):
    """
    Возвращает отсортированный список книг.

    Поддерживает сортировку по любому из допустимых полей (`id`, `title`, `author`, `price`)
    и направлениям: `ascend` (по возрастанию) или `descend` (по убыванию).

    Важно: для предотвращения SQL-инъекций стоит строго ограничить список `filter`.

    Args:
        request (HttpRequest): Объект HTTP-запроса.
        filter (str): Имя поля для сортировки (например, `'title'`).
        direction (str): `'ascend'` или `'descend'`.

    Returns:
        HttpResponse: Рендерит `partial_book_list.html` с отсортированным списком книг.
    """
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookEditForm(request.POST, instance=book)
        if form.is_valid():
            return render(request,
                          'partial_book_detail.html',
                          {'book': book}
                          )
    else:
        form = BookEditForm(instance=book)
    return render(request,
                  'partial_book_update_form.html',
                  {'form': form, 'book': book}
                  )

@require_http_methods(['GET'])
def book_detail(request, pk):

    book = get_object_or_404(Book, pk=pk)
    return render(request,
                  'partial_book_detail.html',
                  {'book': book}
                  )

@require_http_methods(['PATCH'])
def update_book_status(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.read = not book.read
    book.save()
    return render(request,
                  'partial_book_detail.html',
                  {'book': book}
                  )

@require_http_methods(['GET'])
def book_list_sort(request, filter, direction):
    filter_dict = {
        _('id'): 'pk',
        _('title'): 'title',
        _('author'): 'author',
        _('price'): 'price',
        _('read'): 'read',
    }
    if filter in filter_dict:
        if direction == _('descend'):
            book_list = Book.objects.order_by('-' + filter_dict[filter])
        else:
            book_list = Book.objects.order_by(filter_dict[filter])
    else:
        book_list = Book.objects.all()
    return render(
        request,
        'partial_book_list.html',
        {'book_list': book_list}
    )

@require_http_methods(['DELETE'])
def delete_book(request, pk):
    """
    Удаляет книгу по ID.

    Выполняет `DELETE`-запрос и возвращает `204 No Content` (HTMX автоматически
    удалит соответствующую строку из DOM благодаря `hx-swap="delete"`).

    Args:
        request (HttpRequest): Объект HTTP-запроса (ожидается метод DELETE).
        pk (int): ID удаляемой книги.

    Returns:
        HttpResponse: `HttpResponse(status=204)` — пустой ответ для удаления.
    """
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return HttpResponse()


