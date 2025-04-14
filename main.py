from flask import Flask, request import telegram from telegram import Update from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters import os

Hardcoded token

BOT_TOKEN = "8013983070:AAGdnHwfIUV7tr9GwPcrpfF6Ms56zCoYUHI" bot = telegram.Bot(token=BOT_TOKEN)

Flask app

app = Flask(name)

@app.route('/') def index(): return "Bot is running!"

@app.route(f"/{BOT_TOKEN}", methods=['POST']) def webhook(): update = telegram.Update.de_json(request.get_json(force=True), bot) dispatcher.process_update(update) return "OK"

def start(update, context): update.message.reply_text("Send me a chart screenshot for analysis.")

def handle_photo(update, context): update.message.reply_text("Analyzing chart... (this is a mock response)\nTrend: Up\nRSI: Neutral\nSupport found.")

Setup dispatcher

from telegram.ext import Dispatcher dispatcher = Dispatcher(bot, None, use_context=True) dispatcher.add_handler(CommandHandler("start", start)) dispatcher.add_handler(MessageHandler(Filters.photo, handle_photo))

Set webhook on startup (for Render)

@app.before_first_request def set_webhook(): webhook_url = f"https://{os.environ['RENDER_EXTERNAL_HOSTNAME']}/{BOT_TOKEN}" bot.setWebhook(webhook_url)

Flask port

if name == "main": app.run(host='0.0.0.0', port=10000)

