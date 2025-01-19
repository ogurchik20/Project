import sqlite3
from faker import Faker

# Подключение к базе данных
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Инициализация библиотеки Faker
faker = Faker()

# Жанры книг
genres = ['Fiction', 'Non-Fiction', 'Science Fiction', 'Fantasy', 'Mystery', 'Romance', 'Thriller', 'Biography']

# Генерация 500 записей
books = [
    (
        faker.catch_phrase(),
        faker.name(),
        faker.random.choice(genres),
        faker.year()
    )
    for i in range(500)
]

cursor.executemany("INSERT INTO books (title, author, genre, year) VALUES (?, ?, ?, ?)", books)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()