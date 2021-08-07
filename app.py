import os

from flask import Flask, request
import requests


app = Flask(__name__)


def get_weather():
    params = {"query": "Dnipropetrovsk", "access_key": os.environ.get('access_key')}
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    return f"Сейчас в Днепре {api_response['current']['temperature']} градуса(ов)"


def send_message(chat_id, text):
    method = "sendMessage"
    token = os.environ.get('TOKEN')
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)


@app.route("/", methods=["GET", "POST"])
def receive_update():
    if request.method == "POST":
        print(request.json)
        chat_id = request.json["message"]["chat"]["id"]
        weather = get_weather()
        send_message(chat_id, weather)
    return {"ok": True}

