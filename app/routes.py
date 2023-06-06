from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/name/<name>')
@app.route('/name')
def name(name='World'):
    return "Hello, f{name}"

@app.route('/about')
def about():
    return render_template('about.html')

