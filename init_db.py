from models import init_db, get_db_connection

def add_sample_products():
    conn = get_db_connection()
    sample_products = [
        ('Летняя шина Ikon (Nokian Tyres) Autograph Eco 3', 100, 'Летняя шина 205/55 R16 94H XL'),
        ('Двигатель BMW M50', 1300, 'Объем 1991 см³, мощность 150 л.с'),
        ('BMW Крышка бачка расширительного', 12, 'Крышка для бачка расширительного'),
    ]
    conn.executemany('INSERT INTO products (name, price, description) VALUES (?, ?, ?)', sample_products)
    conn.commit()
    
    
    print("=== PRODUCTS ===")
    for row in conn.execute('SELECT * FROM products'):
        print(row['id'], row['name'], row['price'])

    print("\n=== ORDERS ===")
    for row in conn.execute('SELECT * FROM orders'):
        print(dict(row))

    print("\n=== ORDER_ITEMS ===")
    for row in conn.execute('SELECT * FROM order_items'):
        print(dict(row))

    conn.close()

if __name__ == '__main__':
    init_db()
    add_sample_products()
    print("База данных инициализирована!")

    