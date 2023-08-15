import requests

def sentiment(text):
    return requests.post("http://127.0.0.1:5000/predict", json={"text": text}).json()