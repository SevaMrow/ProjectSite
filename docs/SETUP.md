# Установка и запуск (Flask + sqlite3)

## Предпосылки
- Python 3.8+
- Windows: PowerShell

## Локальный запуск
```bash
python -m venv .venv
. .venv/Scripts/activate  # PowerShell: .venv\Scripts\Activate.ps1
pip install -U pip
pip install flask pydantic python-dotenv
```

Создайте структуру проекта:
```text
ProjectSite/
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

Запуск:
```bash
$env:FLASK_APP = "app:create_app"
$env:FLASK_ENV = "development"
flask run --debug
```

## Переменные окружения
- `DATABASE_URL` — C:\Users\admin\Desktop\ProjectSite\database.db
