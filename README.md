Простой микросервис на fastapi.
Проверка работы самой API,
также проверка работы базы данных 
postgres и создание базы данных(если нужно).

Клонирование репозитория:

```share
https://github.com/DmitriiButk/uwai-rest-backend-booking.git
```

Установка зависимостей:

```share
pip install requirements.txt
```

Запуск API:

```share
uvicorn app.main:app --reload
```

Проверка работы API:

```share
http://127.0.0.1:8000/api_health
```

Проверка работы базы данных:

```share
http://127.0.0.1:8000/db_health
```

Создание новой базы данных:

```share
http://127.0.0.1:8000/db_create
```

Если база данных создана, то ответ будет о созданной бд.
