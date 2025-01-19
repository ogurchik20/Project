import sqlite3

# Функция для добавления книги в базу данных
def add_book(title, author, genre, year):
    # Подключаемся к базе данных
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()

    # Вставляем книгу в таблицу books
    cursor.execute('''
    INSERT INTO books (title, author, genre, year) 
    VALUES (?, ?, ?, ?)
    ''', (title, author, genre, year))

    # Сохраняем изменения и закрываем подключение
    conn.commit()
    conn.close()

# Пример добавления книги
add_book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 1925)
print("Книга успешно добавлена!")
