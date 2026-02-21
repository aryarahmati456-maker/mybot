from flask import Flask, request
import requests
import json

app = Flask(__name__)

TOKEN = "HFGBIOFGIVHWMFWHIRXVRNKCRRUWNERZBIS"
API_URL = f"https://botapi.rubika.ir/v3/{TOKEN}"

def send_message(chat_id, text, buttons=None):
    url = API_URL + "/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
        "reply_markup": {
            "inline_keyboard": buttons if buttons else []
        }
    }
    requests.post(url, json=data)

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    if "message" in data:
        chat_id = data["message"]["chat_id"]
        text = data["message"].get("text", "")
        
        if text == "/start":
            buttons = [
                [
                    {"text": "فروشگاه اکانت", "callback_data": "shop"},
                    {"text": "آیدی دستیاران", "callback_data": "helpers"}
                ],
                [
                    {"text": "اطلاعات بنده", "callback_data": "info"},
                    {"text": "مجموعه ما", "callback_data": "group"}
                ]
            ]
            send_message(chat_id, "سلام! انتخاب کنید:", buttons)
        elif text == "/help":
            send_message(chat_id, "برای دریافت راهنمایی، دستور /start رو وارد کنید.")
        else:
            send_message(chat_id, "دستور شناخته نشده است.")
    return "OK"

@app.route("/", methods=["GET"])
def home():
    return "Rubika Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
