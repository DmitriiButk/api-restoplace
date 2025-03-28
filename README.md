# api-restoplace

Микросервис на FastAPI для интеграции с API Restoplace.

## Установка и запуск

### Клонирование репозитория

Для клонирования репозитория используйте следующую команду:

```shell
git clone https://github.com/DmitriiButk/api-restoplace.git
```

### Установка зависимостей

Используйте следующую команду для установки необходимых зависимостей:

```shell
pip install -r requirements.txt
```

### Настройка базы данных

#### Создание базы данных PostgreSQL

Для создания базы данных PostgreSQL выполните следующие шаги:

1. Установите PostgreSQL, если он еще не установлен. Инструкции по установке можно найти на официальном
   сайте [PostgreSQL](https://www.postgresql.org/download/).

2. Создайте новую базу данных и пользователя:

```shell
# Подключитесь к серверу PostgreSQL
psql -U postgres

# Внутри psql выполните следующие команды:
CREATE DATABASE database_name;
CREATE USER user_name WITH ENCRYPTED PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE database_name TO user_name;
```

Замените `database_name`, `user_name` и `your_password` на ваши значения.

### Создание env файла

Создайте файл `.env` в корне проекта и добавьте следующие параметры:

```env
DATABASE_HOST=your_host
DATABASE_PORT=your_port
DATABASE_NAME=your_database_name
DATABASE_USER=your_user_name
DATABASE_PASSWORD=your_password
RESTO_API_KEY=some_api_key
```

Замените `your_host`, `your_port`, `your_database_name`, `your_user_name`, `your_password` и `some_api_key` на ваши
значения.

### Запуск API

Для запуска API используйте следующую команду:

```shell
uvicorn app.main:app --reload
```

## Проверка работы

### Проверка работы API

Для проверки работы API перейдите по следующему URL:

```shell
http://127.0.0.1:8000/api_health
```

### Проверка работы API Restoplace

Для проверки работы API Restoplace перейдите по следующему URL:

```shell
http://127.0.0.1:8000/api_restaurant_health
```

### Проверка работы базы данных

Для проверки работы базы данных перейдите по следующему URL:

```shell
http://127.0.0.1:8000/db_health
```

## Основные компоненты

### Модуль `app.main`

- Основной модуль приложения, содержащий запуск FastAPI и включение роутеров.

### Роутеры

#### Резервы (`app/routers/reserves.py`)

- `/reserves`: Получение списка резервов
- `/reserves/{reserve_id}`: Получение данных резерва по ID
- `/reserves`: Создание резерва
- `/reserves/{reserve_id}/status`: Обновление статуса резерва
- `/times`: Получение доступных слотов времени

#### Залы (app/routers/halls.py)

- `/halls`: Получение списка залов
- `/halls/{hall_id}`: Получение данных зала по ID

#### Объекты бронирования (app/routers/items.py)

- `/items`: Получение списка объектов бронирования
- `/items/{item_id}`: Получение данных объекта бронирования по ID

#### Проверка API Restoplace (`app/routers/restaurant_check.py`)

- `/api_restaurant_health`: Проверка работы API Restoplace

#### Проверка базы данных (`app/routers/db_check.py`)

- `/db_health`: Проверка подключения к базе данных

### Схемы

#### `ReserveCreate` (`app/schemas.py`)

- `from_time`: Начало резерва
- `to`: Конец резерва
- `name`: Имя гостя
- `phone`: Телефон гостя в формате 79876543210
- `email`: Почта гостя
- `count`: Количество человек
- `text`: Комментарий к резерву
- `source`: Источник бронирования (домен)
- `item_ids`: ID бронируемого стола или столов
- `waitlist`: Заявка попадет в Лист ожидания
- `deposit`: Учитывать депозит при бронировании

## Тестирование

### Запуск тестов

Для запуска тестов используйте команду:

```bash
pytest
```
