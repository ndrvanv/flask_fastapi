import random

from flask import Flask, render_template
from models import db, Books, Authors, BookAuthor

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")


@app.cli.command("add-book")
def add_book():
    for i in range(15):
        book = Books(
            name=f"name_{i}",
            realized_year=2000 + i,
            copies=100 * i,
        )
        db.session.add(book)
    for j in range(10):
        author = Authors(firstname=f"firstname_{i}", lastname=f"lastname_{i}")
        db.session.add(author)
    for k in range(10):
        book_author = BookAuthor(
            id_book=random.randint(1, 14), id_author=random.randint(1, 9)
        )
        db.session.add(book_author)
    db.session.commit()
    print("data_added")


@app.get("/")
def get_books():
    books = Books.query.all()
    context = {"books": books}
    return render_template("books.html", **context)
