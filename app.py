from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template('home.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/<string:post_name>')
def post(post_name=None):
    return render_template('post.html')


@app.route('/add_post')
def add_post():
    return render_template('add_post.html')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
