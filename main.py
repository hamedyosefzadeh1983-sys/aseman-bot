import os
import telebot
from flask import Flask
import threading

TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TELEGRAM_TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ ربات مرکز خدمات آسمان فعال است!"

def run_bot():
    print("🤖 ربات تلگرام شروع به کار کرد...")
    bot.polling()

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    btn1 = telebot.types.KeyboardButton('🛠️ خدمات')
    btn2 = telebot.types.KeyboardButton('💰 تعرفه‌ها')
    btn3 = telebot.types.KeyboardButton('📞 تماس با ما')
    markup.add(btn1, btn2, btn3)
    
    bot.send_message(
        message.chat.id,
        "🌐 **به مرکز خدمات هوشمند آسمان خوش آمدید!**\n\nلطفاً گزینه مورد نظر را انتخاب کنید:",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message:
