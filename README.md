# Лабораторная работа 2 — страницы Django

Учебный проект содержит HTML-страницу о торговых помещениях, списки, таблицу и оформление CSS. Отдельные адреса показывают одинаковое приветствие с типом ответа `text/plain` и `text/html`.

## Запуск

При установленном Python 3.11 из корня проекта в PowerShell:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src/firstwebpage/manage.py migrate
.\.venv\Scripts\python.exe src/firstwebpage/manage.py test flatpages
.\.venv\Scripts\python.exe src/firstwebpage/manage.py runserver
```

Главная страница находится по адресу `http://127.0.0.1:8000/`. Страница без внешних стилей доступна по адресу `/template/`, варианты приветствия — `/hello/` и `/hello/plain/`.

`src/firstwebpage/flatpages/` содержит представления, тесты, шаблоны и статические файлы. Значения в таблице учебные. Для локального запуска можно задать `DJANGO_SECRET_KEY`; если переменная не задана, ключ создаётся при запуске и вход в административную панель после перезапуска может потребовать повторной авторизации.
