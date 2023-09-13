from pathlib import PurePath, Path


from flask import (
    Flask,
    render_template,
    request,
    abort,
    url_for,
    redirect,
    flash,
    make_response,
)
from werkzeug.utils import secure_filename
from markupsafe import escape

# tasks_1_4
# Создать страницу, на которой будет кнопка "Нажми меня", при
# нажатии на которую будет переход на другую страницу с
# приветствием пользователя по имени.

# tasks_2_5
# Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.

# tasks_3_6
# Создать страницу, на которой будет форма для ввода логина
# и пароля
# При нажатии на кнопку "Отправить" будет произведена
# проверка соответствия логина и пароля и переход на
# страницу приветствия пользователя или страницу с
# ошибкой.

# task_4
# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.

# task_5
# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.

# task_6
# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

# task_7
# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

# task_8
# Создать страницу, на которой будет форма для ввода имени
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с flash сообщением, где будет
# выведено "Привет, {имя}!".

# task_9
# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.


app = Flask(__name__)


@app.route("/")
def base():
    return render_template("base.html")


app.secret_key = b"5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4"


@app.route("/next")
def tap_me():
    return "Привет Вася"


@app.route("/upload/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files.get("file")
        file_name = secure_filename(file.filename)
        file.save(PurePath.joinpath(Path.cwd(), "uploads", file_name))
        return f"Файл {escape(file_name)} загружен на сервер"
    context = {"task": "Задание_2"}
    return render_template("page_1.html", **context)


@app.route("/authorization/", methods=["GET", "POST"])
def authorization():
    if request.method == "POST":
        login = {"auth_email": "qwe@ya.ru", "auth_pass": "123"}
        auth_email = request.form.get("auth_email")
        auth_pass = request.form.get("auth_pass")
        if auth_email == login["auth_email"] and auth_pass == login["auth_pass"]:
            return f"Вход из почты: {escape(auth_email)} выполнен успешно"
        else:
            return f"Ошибка входа с почтой {auth_email}"
    context = {"task": "Задание_2"}

    return render_template("authorization.html", **context)


@app.route("/counter/", methods=["GET", "POST"])
def counter():
    if request.method == "POST":
        text = request.form.get("text")
        return f"Количество слов: {escape(len(text.split()))}"
    context = {"task": "Задание_4"}
    return render_template("counter.html", **context)


@app.route("/calculate/", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        number_1 = request.form.get("number_1")
        number_2 = request.form.get("number_2")
        operation = request.form.get("operation")

        match operation:
            case "add":
                return str(int(number_1) + int(number_2))
            case "subtract":
                return str(int(number_1) - int(number_2))
            case "multiply":
                return str(int(number_1) * int(number_2))
            case "divide":
                if str(int(number_2)) == str(0):
                    return f"На ноль делить нельзя!"
                return str(int(number_1) / int(number_2))

    context = {"task": "Задание_5"}
    return render_template("calculate.html", **context)


@app.errorhandler(403)
def page_not_found(e):
    context = {
        "title": "Доступ не разрешен",
        "url": request.base_url,
    }
    return render_template("403.html", **context), 403


@app.route("/profile/", methods=["GET", "POST"])
def profile():
    MIN_AGE = 18
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        if int(age) > MIN_AGE:
            return f"Ваше имя {name} и ваш возраст {age} лет, вам доступ разрешен"

        abort(403)
    context = {"task": "Задание_4"}
    return render_template("profile.html", **context)


@app.route("/squere/", methods=["GET", "POST"])
def squere():
    num = 4
    return redirect(url_for("num_squere", number=int(num**2)))


@app.route("/squere/<int:number>")
def num_squere(number: int):
    return str(number)


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Проверка данных формы
        if not request.form["name"]:
            flash("Введите имя!", "danger")
            return redirect(url_for("form"))
        # Обработка данных формы
        flash("Форма успешно отправлена!", "success")
        return redirect(url_for("form"))
    return render_template("form.html")


@app.route("/cookies", methods=["GET", "POST"])
def cookies():
    if request.method == "POST":
        context = {"title": "main", "name": request.form.get("username")}
        name = request.form.get("username")
        response = make_response(render_template("index.html", **context))
        response.set_cookie(name, "User")
        return response
    context = {"title": "cookies"}
    return render_template("cookies.html", **context)
    # Ошибка при запуске


@app.route("/delete_cookies", methods=["GET", "POST"])
def delete_cookies():
    context = {"title": "cookies"}
    response = make_response(render_template("index.html", **context))
    response.set_cookie(*request.cookies, expires=0)
    return response


if __name__ == "__main__":
    app.run(debug=True)
