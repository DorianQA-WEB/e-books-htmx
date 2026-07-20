"""
Конфигурация URL-адресов для проекта django_htmx.

Описание:
    Этот модуль определяет корневой маршрут URL и подключает маршруты приложений.
    Все запросы к корневому пути ('/') перенаправляются в маршруты приложения `books`.

Структура:
    - admin/ — административная панель Django (автоматически сгенерирована).
    - '' (корневой путь) — включает URL-шаблоны из приложения `books` (см. `books/urls.py`).
Примеры:
    Приложение `books` обрабатывает следующие пути:
        /                          → отображение списка книг (book_list)
        /create_book/              → добавление новой книги (create_book)
        /update_book_details/<id>/ → редактирование книги (update_book_details)
        /delete_book/<id>/         → удаление книги (delete_book)
        /toggle_read/<id>/         → переключение статуса "прочитано"
        /book_list_sort/<field>/<direction>/ — сортировка списка
Атрибуты:
    urlpatterns (list): Список объектов `path()`, сопоставляющих URL-адреса с view-функциями.

Примечания:
    Для корректной работы административной панели выполните:
        python manage.py migrate
        python manage.py createsuperuser

    Чтобы включить переводы интерфейса, убедитесь, что в `settings.py`:
        - `USE_I18N = True`
        - `LOCALE_PATHS = [BASE_DIR / 'locale']`
        - существуют `.po` файлы и выполнена команда `compilemessages`.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('', include('books.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
)
