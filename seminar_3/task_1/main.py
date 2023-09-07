import random

from flask import Flask, render_template
from models import db, Students, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.cli.command('add-students')
def add_db():
    for j in range(3):
        faculty = Faculty(
            name=f'faculty_{j}'
        )
        db.session.add(faculty)
    age_student = 15
    for i in range(12):
        student = Students(
            firstname=f'firstname_{i}',
            lastname=f'lastname_{i}',
            age=age_student + i,
            gender=random.choice(['male', 'female']),
            group=random.randint(1, 3),
            id_faculty=random.randint(0, 2)
        )

        db.session.add(student)
    db.session.commit()
    print('Данные добавлены')


@app.get('/')
def get_students():
    students = Students.query.all()
    context = {
        'students': students
    }
    return render_template('students.html', **context)
