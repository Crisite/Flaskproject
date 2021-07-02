from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField, PasswordField
from wtforms.validators import Length, EqualTo


class RegisterForm(Form):
    username = StringField(validators=[Length(3, 20)])
    password = StringField(validators=[Length(6, 20)])
    password_repeat = StringField(validators=[EqualTo("password")])
    telephone = StringField(validators=[Length(11, 11)])
    address = StringField(validators=[Length(0, 20)])


class LoginForm(Form):
    username = StringField(validators=[Length(3, 20)])
    password = StringField(validators=[Length(6, 20)])

