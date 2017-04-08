from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):
    user_id = StringField('user_id', validators=[DataRequired()])
    user_name = StringField('user_name', validators=[Length(min=0, max=30)])
    password = StringField('password', validators=[Length(min=0, max=30)])
