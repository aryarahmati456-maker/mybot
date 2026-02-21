from flask import Flask, request
import requests
import json

app = Flask(__name__)

TOKEN = "HFGBIOFGIVHWMFWHIRXRVRNKCRRUWNKERZBIS"
API_URL = f"https://botapi.rubika.ir/v3/{TOKEN}"

def send_message(chat_id, text):
    url = API_URL + "/sendMessage"
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
        
        # اضافه کردن دستورات جدید
        if text == "/start":
    elif text == "/مجموعه خبری ما":
    send_message(کلیک کن, "@MaJMoeH_PERSiAN") 
            send_message(chat_id, "ربیکا هستم! برای کمک، دستور /help رو بزن!")
        elif text == "/help":
            send_message(chat_id, "این ربات از دستورات زیر پشتیبانی می‌کنه:\n/start: شروع کار\n/help: برای راهنمایی")
        else:
            send_message(chat_id, "دستور شناخته شده‌ای ارسال نکردی. برای کمک، /help رو بزن!")

    return "OK"

@app.route("/", methods=["GET"])
def home():
    return "Rubika Bot is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
