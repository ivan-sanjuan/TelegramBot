import telebot
import os
from stock_utils import symbol_handler
from stock_utils import book_handler
from book_scraper import search_book
from stats_scraper import get_stats

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)
print(f"Your bot token is: {API_KEY}")
print('"Beanie is swimming..."')
bot.remove_webhook()

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
        
@bot.message_handler(commands=['book'])
def bot_book_search(message):
    try:
        input = message.text.split(maxsplit=1)[1].strip()
        data = book_handler(input)
        book_results = search_book(data)
        print(f"Received command: {message.text}")
        for entry in book_results:
            response = (
                f"📚{entry['📚Title']}\n"
                f"👤 Author: {entry['Author']}\n"
                f"🈯 Language: {entry['Language']}\n"
                f"📄 Format: {entry['Ext.']} — {entry['Filesize']}\n"
                f"{entry['🔽Download Link🔽']}\n"
            )
            bot.send_message(message.chat.id, f'{response}\n+1 ISPAM 🐧🐧', disable_web_page_preview=True)

    except IndexError:
        bot.reply_to(message, "Anong book mama? ganto format '/book little women' 🐧🐧")


bot.polling()

