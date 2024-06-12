from flask import Flask, render_template

from config import Config
from forms import AddPostForm
from models import category

config = Config

app = Flask(__name__)
app.config.from_object(config)

category.db.init_app(app)


@app.route('/')
def home():
    return render_template('home.html', title='Домашняя страница')


@app.route('/blog')
def blog():
    return render_template('blog.html', title='Блог')


@app.route('/<string:post_name>')
def post(post_name=None):
    return render_template('post.html')


@app.route('/add_post')
def add_post():
    categories = category.Category.getCategoryValues()
    form = AddPostForm()
    form.category.choices = categories
    return render_template('add_post.html', title='Добавить пост', form=form)


@app.route('/about')
def about():
    return render_template('about.html', title='О сайте')


if __name__ == '__main__':
    app.run(debug=True)
