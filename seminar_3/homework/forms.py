from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    email = StringField('Почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[validators.DataRequired()])
    confirm_password = PasswordField('Подтверждение пароля', validators=[validators.DataRequired(), validators.EqualTo('password', message='Пароли должны совпадать')])
    submit = SubmitField("Зарегестрироваться")
