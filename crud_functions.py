import sqlite3

connection = sqlite3.connect('initiate_db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
)
''')

#cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users(email)')

for i in range(1, 5):
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)',
                   (f'Продукт{i}', f'Описание{i}', f'{i}00'))


def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()


cursor.execute('SELECT * FROM Products')
products = cursor.fetchall()
for product in products:
    print(f'Название продукта: {product[0]} | Описание: {product[1]} | Цена: {product[2]}')


connection.commit()
#connection.close()
