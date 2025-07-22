import telebot
import os
from stock_utils import symbol_handler
from stats_scraper import get_stats

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)
print("Beanie is swimming...")

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


bot.polling()
