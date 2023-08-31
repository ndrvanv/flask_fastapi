from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello world!"


@app.route("/about/")
def about():
    return "about"


@app.route("/contact/")
def contact():
    return "contact"


@app.route("/<int:num_1>/<int:num_2>")
def sum_num(num_1: int, num_2: int) -> str:
    return str(num_1 + num_2)


@app.route("/string/<string:text>")
def len_text(text: str):
    return str(len(text))


@app.route("/first/")
def first():
    return render_template("index.html")


@app.route('/students/')
def students():
    head = {
        'firstname': "Имя",
        "lastname": "Фамилия",
        'age': 'Возраст',
        'rating': 'Средний балл'

    }
    students_list = [
        {
            'firstname': "Иван",
            "lastname": "Иванов",
            'age': 25,
            'rating': 4.5
        },

        {

            'firstname': "Антон",
            "lastname": "Антовнов",
            'age': 23,
            'rating': 5

        },

        {
            'firstname': "Василий",
            "lastname": "Васильев",
            'age': 20,
            'rating': 4
        }
    ]
    return render_template('students.html', **head, students_list=students_list)


@app.route("/news/")
def news():
    block_news = [
        {
            'title': "новость_1",
            "description": "описание_1",
            'created_at': datetime.now().strftime("%H:%M - %m.%d.%Y года"),
        },

        {

            'title': "новость_2",
            "description": "описание_2",
            'created_at': datetime.now().strftime("%H:%M - %m.%d.%Y года"),

        },

        {
            'title': "новость_3",
            "description": "описание_3",
            'created_at': datetime.now().strftime("%H:%M - %m.%d.%Y года"),
        }
    ]

    return render_template('news.html', block_news=block_news)


if __name__ == "__main__":
    app.run(debug=True)
