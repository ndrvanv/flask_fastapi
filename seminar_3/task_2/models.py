from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Задание №2
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    realized_year = db.Column(db.Integer, nullable=False)
    copies = db.Column(db.Integer, nullable=False)
    id_author = db.Column(db.Integer, db.ForeignKey('authors.id'))
    authors = db.relationship('Authors', secondary='book_author', backref='books', lazy=True)

    def __repr__(self):
        return f'Books({self.name} {self.realized_year} {self.copies} )'


class Authors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)

    # Возможно лишнее
    # books = db.relationship("Books", backref='author', lazy=True)

    def __repr__(self):
        return f'Author({self.firstname}, {self.lastname})'


class BookAuthor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_book = db.Column(db.Integer, db.ForeignKey('books.id'))
    id_author = db.Column(db.Integer, db.ForeignKey('authors.id'))
