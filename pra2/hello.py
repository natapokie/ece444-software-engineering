from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

import os

app = Flask(__name__)

# use os to generate a secret key
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

class NameForm (FlaskForm): 
    name = StringField('What is your name?', validators=[DataRequired()]) 
    submit = SubmitField('Submit')

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
@app.route('/', methods=['GET', 'POST'])
def index():
    # EXAMPLE 3-13 adding a datetime variable
    print(datetime.utcnow())

    # EXAMPLE 4-4 handle webform with GET and POST request methods
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=name)

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

if __name__ == '__main__':
    app.run(debug=True)