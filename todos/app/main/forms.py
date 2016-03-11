from flask.extwtf import Form
from wtforms import StringField, SubmitField, BooleanField, TextAreaField, PasswordField
from wtforms.validators import Required


class TodoForm(Form):
    review = StringField('your review: ')

