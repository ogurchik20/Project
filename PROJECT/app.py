from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


# Функция для подключения к базе данных
def get_db_connection():
    conn = sqlite3.connect('library.db')
    conn.row_factory = sqlite3.Row  # Это позволяет обращаться к данным по имени столбца
    return conn


# Главная страница - список всех книг
@app.route('/')
def index():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return render_template('index.html', books=books)


# Страница добавления книги
@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        year = request.form['year']

        conn = get_db_connection()
        conn.execute('INSERT INTO books (title, author, genre, year) VALUES (?, ?, ?, ?)',
                     (title, author, genre, year))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))  # Перенаправление на главную страницу
    return render_template('add.html')  # Отображение формы для добавления книги


# Страница редактирования книги
@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit(id):
    conn = get_db_connection()
    book = conn.execute('SELECT * FROM books WHERE id = ?', (id,)).fetchone()  # Получение данных книги по ID

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        year = request.form['year']

        # Обновление информации о книге в базе данных
        conn.execute('UPDATE books SET title = ?, author = ?, genre = ?, year = ? WHERE id = ?',
                     (title, author, genre, year, id))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))  # Перенаправление на главную страницу после сохранения изменений

    conn.close()
    return render_template('edit.html', book=book)  # Отображение формы с данными книги для редактирования


# Удаление книги
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM books WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))  # Перенаправление на главную страницу после удаления


if __name__ == '__main__':
    app.run(debug=True)
