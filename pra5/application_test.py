import pytest
from application import application, load_model
import time

@pytest.fixture
def client():
    application.config["TESTING"] = True
    with application.app_context():
        load_model()
        yield application.test_client()

def test_real_news1(client):
    response = client.post(
        "/predict",
        json={"text": "Young voters in key election battlegrounds are being recommended fake AI-generated videos featuring party leaders, misinformation, and clips littered with abusive comments, the BBC has found."},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert response.json.get('prediction') == 'REAL'

def test_real_news2(client):
    response = client.post(
        "/predict",
        json={"text": "The head of the Canadian Broadcasting Corp. is facing scrutiny from members of a House of Commons committee for her roughly $6,000 worth of travel and hotel expenses at the Paris Olympics this past summer."},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert response.json.get('prediction') == 'REAL'


def test_fake_news1(client):
    response = client.post(
        "/predict",
        json={"text": "Local Cat Becomes Overnight's Sensation After Saving a Child from a Dog Attack"},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert response.json.get('prediction') == 'FAKE'


def test_fake_news2(client):
    response = client.post(
        "/predict",
        json={"text": "In a shocking study released by the Institute of Absurd Science, researchers have concluded that chocolate can be classified as a vegetable because it comes from cocoa beans. This revelation has led to a nationwide surge in chocolate sales, with the government now recommending three servings of chocolate daily for a balanced diet. Health experts are still debating how to work this into the food pyramid."},
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert response.json.get('prediction') == 'FAKE'
