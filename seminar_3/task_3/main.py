from flask import Flask, render_template, request
from flask_wtf import CSRFProtect
from models import db, Users
from forms import RegisterForm

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
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        username = form.username.data
        email = form.email.data
        pwd = form.pwd.data
        user = Users(username=username, email=email, pwd=pwd)
        db.session.add(user)
        db.session.commit()
        return f'Вы успешно зарегестрированы'
    return render_template('register.html', form=form)

@app.route('/users/', methods=['GET', 'POST'])
def get_users():
    users = Users.query.all()
    return f"{list(users)}"
