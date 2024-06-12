from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from config import Config

config = Config

app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)

from models.post import Post
from models.category import Category



@app.route('/')
def home():
    with app.app_context():
        db.create_all()
    return render_template('home.html', title='Домашняя страница')


@app.route('/blog')
def blog():
    return render_template('blog.html', title='Блог')


@app.route('/<string:post_name>')
def post(post_name=None):
    return render_template('post.html')


@app.route('/add_post')
def add_post():
    return render_template('add_post.html', title='Добавить пост')


@app.route('/about')
def about():
    return render_template('about.html', title='О сайте')


if __name__ == '__main__':
    app.run(debug=True)
