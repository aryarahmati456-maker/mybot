from flask import Flask, request
import requests
import json

app = Flask(name)

# توکن ربات خود را اینجا وارد کنید
TOKEN = "HFGBI0FGIVHWMFWHIRXRVRNKCRRUWNKERZBBISKGCQJJIRRNBVCLNHRQFOOHFPUX"
API_URL = f"https://botapi.rubika.ir/v3/{TOKEN}"

# تابع ارسال پیام
def send_message(chat_id, text, buttons=None):
    url = API_URL + "/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
        "reply_markup": json.dumps({
            "inline_keyboard": buttons if buttons else []
        })
    }
    requests.post(url, json=data)

# تنظیم Webhook برای دریافت پیام‌ها
@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    if "message" in data:
        chat_id = data["message"]["chat_id"]
        text = data["message"].get("text", "")
        
        # دستور /start
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
        
        # دستور /help
        elif text == "/help":
            send_message(chat_id, "این ربات از دستورات زیر پشتیبانی می‌کند:\n/start: شروع\n/help: راهنمایی\n/command1: توضیح دستور 1\n/command2: توضیح دستور 2")
        
        # دستورات سفارشی شما
        elif text == "/command1":
            send_message(chat_id, "این دستور شماره 1 است.")
        elif text == "/command2":
            send_message(chat_id, "این دستور شماره 2 است.")
        else:
            send_message(chat_id, "دستور شناخته نشده است.")
    
    return "OK"

# پاسخ به کلیک دکمه‌ها (callback_query)
@app.route("/callback", methods=["POST"])
def callback():
    data = request.json
    if "callback_query" in data:
        callback_query_id = data["callback_query"]["id"]
        chat_id = data["callback_query"]["message"]["chat"]["id"]
        callback_data = data["callback_query"]["data"]

        # عمل بر اساس داده دکمه‌ها
        if callback_data == "shop":
            send_message(chat_id, "شما به فروشگاه اکانت وارد شدید!")
        elif callback_data == "helpers":
            send_message(chat_id, "دستیاران ربات.")
        elif callback_data == "info":
            send_message(chat_id, "اطلاعات شما به روزرسانی شد.")
        elif callback_data == "group":
            send_message(chat_id, "گروه ما.")
    
    return "OK"

# راه‌اندازی سرور
if name == "main":
    app.run(host="0.0.0.0", port=5000)
