from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application = Flask(__name__)
application.config['SECRET_KEY'] = 'your secret key'

model = None
vectorizer = None

class NewsForm(FlaskForm): 
    text = TextAreaField('Input fake news', validators=[DataRequired()])
    submit = SubmitField('Submit')

def load_model():
    # access global vars
    global model, vectorizer
    
    print('Loading model and vectorizer...')

    # model
    with open('./models/basic_classifier.pkl', 'rb') as f:
        model = pickle.load(f)

    # vectorizer
    with open('./models/count_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)

    # prediction = load_model.predict(vectorizer.transform(['I love this movie']))
    # print(prediction)

@application.route('/', methods=['GET', 'POST'])
def index():

    if (model is None) or (vectorizer is None):
        load_model()

    form = NewsForm()
    prediction = None

    if request.method == 'POST' and form.validate_on_submit():
        print('Form submitted')
        text = form.text.data

        response = application.test_client().post('/predict', json={'text': text})
        prediction = response.json.get('prediction')

    return render_template('index.html', form=NewsForm(), prediction=prediction)

@application.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    text = data.get('text')

    prediction = model.predict(vectorizer.transform([text]))[0]
    return {'prediction': prediction}


@application.route('/result')
def result():
    user_text = request.args.get('user_text')
    prediction = request.args.get('prediction')

    return render_template('result.html', user_text=user_text, prediction=prediction)

if __name__ == '__main__':
    application.run()