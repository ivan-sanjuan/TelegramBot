import telebot
import os
from stock_utils import symbol_handler
from stock_utils import book_handler
from book_scraper import search_book
from stats_scraper import get_stats
from stats_news_scraper import get_news
from div_yield import search_div

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)
print('"Beanie is swimming..."')
bot.remove_webhook()

@bot.message_handler(commands=['stock'])
def handle_stock(message):
    try:
        symbol = message.text.split(maxsplit=1)[1].upper().strip()
        data = symbol_handler(symbol)
        print(f"Symbol parsed: {symbol}")
        stats = get_stats(symbol)
        print(f"Received command: {message.text}")
        response =(
        f'Eto istats papa:\n\n'
        f'📈Stock: {data}\n'
        f'🏷️Price Today: ₱{stats.get('Price Today')} | {stats.get('Change')}\n'
        f'{stats.get('Date Change')}\n\n'
        f'📊PE Ratio: {stats.get('PE Ratio')}\n'
        f'💸PS Ratio: {stats.get('PS Ratio')}\n'
        f'📏PEG: {stats.get('PEG Ratio')}\n'
        f'🏦Return-on-Equity {stats.get('Return on Equity')}\n'
        
        f'/stocknews') 
                    
        bot.send_message(message.chat.id, f'{response}\n\n+1 ISPAM 🐧🐧')
        
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
                f"📚{entry['Title']}\n"
                f"👤 Author: {entry['Author']}\n"
                f"🈯 Language: {entry['Language']}\n"
                f"📄 Format: {entry['Ext.']} — {entry['Filesize']}\n"
                f"https://z-library.sk{entry['Download Link']}\n"
            )
            bot.send_message(message.chat.id, f'{response}\n+1 ISPAM 🐧🐧', disable_web_page_preview=True)

    except IndexError:
        bot.reply_to(message, "Anong book mama? ganto format '/book little women' 🐧🐧")

@bot.message_handler(commands=['stocknews'])
def handle_stock(message):
    try:
        symbol = message.text.split(maxsplit=1)[1].upper().strip()
        data = symbol_handler(symbol)
        news = get_news(symbol)
        response = (
        f'eto bawita sa {data} papa:\n\n'
        f'📅{news.get('date')}\n'
        f'🐧{news.get('title')}\n\n'
        f'{news.get('summary')}\n'
        f'{news.get('news_link')}\n'
        )
        
        bot.send_message(message.chat.id, f'{response}\n+1 ISPAM 🐧🐧')
        
    except IndexError:
        bot.reply_to(message, "wawa siwang news papa wag ka makuwit haaa")
        
@bot.message_handler(commands=['div'])
def handle_stock(message):
    try:
        symbol = message.text.split(maxsplit=1)[1].upper().strip()
        data = symbol_handler(symbol)
        divs = search_div(data)
        response = divs.to_string()
        bot.send_message(message.chat.id, f'{response} +50 ispammm🐧🐧')
    except IndexError:
        bot.reply_to(message, 'wawa siwang dimbidend papa')

bot.polling(none_stop=True)

