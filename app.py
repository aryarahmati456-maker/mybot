from flask import Flask, request
import requests
import json

app = Flask(__name__)

TOKEN = "HFGBI0FGIVHWMFWHIRXRVRNKCRRUWNKERZBBISKGCQJJIRRNBVCLNHRQFOOHFPUX"
API_URL = f"https://botapi.rubika.ir/v3/{TOKEN}/"

def send_message(chat_id, text):
    url = API_URL + "sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text
    }
    requests.post(url, json=data)

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    if "message" in data:
        chat_id = data["message"]["chat_id"]
        text = data["message"].get("text", "")

        if text == "/start":
            send_message(chat_id, "سلام 👋 من ربات روبیکا هستم!")
        else:
            send_message(chat_id, "پیامت رسید 😊")

    return "OK"

@app.route("/", methods=["GET"])
def home():
    return "Rubika Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
