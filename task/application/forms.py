from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

class TaskForm(FlaskForm):
    task_name = StringField("Task")
    completed = BooleanField("Completed", default=False)
    submit = SubmitField("Submit")