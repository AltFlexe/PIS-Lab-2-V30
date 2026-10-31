# Лабораторная работа № 2 — Страницы Django

Созданы страницы с HTML, списками, таблицей и CSS. Вариант № 30 — «Сдача в аренду торговых площадей».

## Запуск

Установите Python 3.11 и выполните в PowerShell из папки проекта:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe src/firstwebpage/manage.py migrate
.\.venv\Scripts\python.exe src/firstwebpage/manage.py runserver
```

Откройте http://127.0.0.1:8000/.
