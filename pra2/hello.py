from flask import Flask
app = Flask(__name__)

# defines application instance and a single route and view function.
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# dynamic url in browser, presented with a personalized greeting that includes the name provided in the URL
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)