from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import CSRFProtect
from werkzeug.security import generate_password_hash

from models import db, Users
from seminar_3.homework.forms import RegisterForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        hash_password = generate_password_hash(form.password.data)
        new_user = Users(
            username=form.username.data,
            email=form.email.data,
            password=hash_password
        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('success'))
    return render_template('register.html', form=form)

@app.route('/users/', methods=['GET', 'POST'])
def get_users():
    users = Users.query.all()
    return f"{list(users)}"

@app.route('/success/')
def success():
    return 'Регистрация прошла успешно'