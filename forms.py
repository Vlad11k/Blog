from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField
from wtforms.validators import Length, DataRequired


class AddPostForm(FlaskForm):
    title = StringField('Название', validators=[DataRequired(), Length(min=5, max=255)])
    content = TextAreaField('Содержание', validators=[Length(min=10)])
    photo = FileField('Изображение', validators=[FileRequired()])
    category = SelectField('Категория',
                           validators=[DataRequired()])
    is_published = BooleanField('Опубликовать', default=True)
    submit = SubmitField('Добавить')
