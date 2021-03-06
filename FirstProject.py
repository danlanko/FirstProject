from flask import Flask, render_template, flash, redirect, session, logging, url_for
from data import Articles
#from flask_sqlalchemy import SQLAlchemy
"""
SQLAlchemy Installed but not enough time to implement, had to take a break.. But still reading about it
So, i had to call my Data's from a dictionary

"""


app = Flask(__name__)

# db = SQLAlchemy(app)

Articles = Articles()


@app.route('/')
def home():
    return render_template('home.html', )

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)


if __name__ == '__main__':
    app.run(debug=True)
