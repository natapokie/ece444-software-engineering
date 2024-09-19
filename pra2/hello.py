from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)

# EXAMPLE 3-4 Flask-Bootstrap initialization
bootstrap = Bootstrap(app)
moment = Moment(app)

# EXAMPLE 2-1
# defines application instance and a single route and view function.
# @app.route('/')
# def index():
#     return '<h1>Hello World!</h1>'

# EXAMPLE 2-2
# dynamic url in browser, presented with a personalized greeting that includes the name provided in the URL
# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, {}!</h1>'.format(name)

# EXAMPLE 3-3 Rendering template
@app.route('/')
def index():
    # EXAMPLE 3-13 adding a datetime variable
    print(datetime.utcnow())
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# EXAMPLE 3-6 Custom error pages
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
