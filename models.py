import sqlite3

# метод создания таблицы
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
# подключение к базе данных
def init_db():
    conn = get_db_connection()
    
    # Таблица товаров
    conn.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT
        )
    ''')
    
    # Таблица заказов
    conn.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name_user TEXT,
            email TEXT,
            number TEXT,
            text TEXT
        )
    ''')
    
    conn.commit()
    conn.close()