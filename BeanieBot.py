import telebot
import os
from stock_utils import symbol_handler
from stock_utils import book_handler
from book_scraper import search_book
from stats_scraper import get_stats
from flask import Flask
from threading import Thread

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

app = Flask('')

@app.route('/')
def home():
    return "Beanie is swimming..."

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

@bot.message_handler(commands=['stock'])
def handle_stock(message):
    try:
        symbol = message.text.split()[1].upper()
        data = symbol_handler(symbol)
        stats = get_stats(symbol)
        print(f"Received command: {message.text}")
        response = f'''Eto istats papa:\n
        📈Stock: {data}\n
        📊PE Ratio: {stats.get('PE Ratio')}
        💸PS Ratio: {stats.get('PS Ratio')}
        📏PEG: {stats.get('PEG Ratio')}
        🏦Return-on-Equity {stats.get('Return on Equity')}
        '''
        bot.reply_to(message, response)

    except IndexError:
        bot.reply_to(message, "Anong istock papa? 🐧🐧 ganto format '/stock BPI'")
        
@bot.message_handler(commands=['books'])
def handle_stock(message):
    try:
        input = message
        data = book_handler(input)
        book_results = search_book(data)
        print(f"Received command: {message.text}")
        response = f'''Eto yung books mama, ispam ko?:\n
        {book_results}
        '''
        bot.reply_to(message, *response)

    except IndexError:
        bot.reply_to(message, "Anong book mama buwwito? 🐧🐧 ganto format '/books little women'")


keep_alive()
bot.polling(non_stop=True)

