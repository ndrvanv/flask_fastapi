from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired(), Email()])
    password = StringField("pwd", validators=[DataRequired()])
    confirm_password = StringField(
        "confirm_pwd", validators=[DataRequired(), EqualTo("pwd")]
    )
