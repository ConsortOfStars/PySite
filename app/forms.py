from flask.ext.wtf import Form
from wtforms.fields import TextField, BooleanField, PasswordField
from wtforms import validators

class RegistrationForm(Form):
    username = TextField('username', [
        validators.InputRequired(message='This is a required field.'),
        validators.Length(min=6,max=12)
    ])
    email = TextField('email_address', [
        validators.InputRequired(message='This is a required field.'),
        validators.Email(message='Not a valid email address.'),
        validators.Length(min=8,max=40)
    ])
    password = PasswordField('new_password', [
        validators.InputRequired(message='This is a required field.'),
        validators.Length(min=8,max=128),
        validators.EqualTo('confirm', message='Passwords must match.')
    ])
    confirm = PasswordField('repeat_password')
    accept = BooleanField('accept_tos', [
        validators.InputRequired(message='This is a required field.')
    ], default=False)
    remember = BooleanField('remember_me', default=False)

class LoginForm(Form):
    username = TextField('username', [
        validators.InputRequired(message='This is a required field.'),
        validators.Length(min=6,max=12,message='That username is too short.')
    ])
    password = PasswordField('password', [
        validators.InputRequired(message='This is a required field.')
    ])
    remember = BooleanField('remember_me', default=False)
