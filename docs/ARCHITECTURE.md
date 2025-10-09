# Архитектура

## Обзор
Простой интернет‑магазин с прямым оформлением заказа:
- Каталог товаров (листинг, карточка)
- Кнопка «Купить» ведет на `checkout` с выбранным SKU
- Оформление и сохранение заказа без корзины

## Компоненты
```text
app/
├── __pycache__    #кэш питона
    ├──app.cpython-39.pyc
    ├──models.cpython-39
    └──models.cpython-313.pyc
├── static        #Хранение для будущего css и изображений
    └──img
        └──Screenshot8480.png
├── templates    # Сайты страничек html
    ├──aboutus.html
    ├──admin.html
    ├──base.html
    ├──catalog.html
    ├──company.html
    ├──index.html
    ├──meny.html
    └──order.html
├── app.py      # Файл запуска
├── database.db # База данных
├── init_db.py  # Добавление данных в базу данных
├── models.py   # Хранение вида базы данных
└──README.md    # файл описание
```

## Схема БД (sqlite3)
```sql
CREATE TABLE IF NOT EXISTS products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  price REAL NOT NULL,
  description TEXT
);
CREATE TABLE IF NOT EXISTS orders (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name_user TEXT,
  email TEXT,
  number TEXT,
  text TEXT
);
```

## Потоки
1. Пользователь открывает `/catalog` → видит товары
2. Нажимает «Купить» → редирект на `/order/<id>`
3. Заполняет форму → POST `/ortder/<id>` → создаются записи в `orders`