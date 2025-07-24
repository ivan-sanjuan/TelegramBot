import requests
from bs4 import BeautifulSoup
import pprint


def get_news(symbol):
    url = f'https://stockanalysis.com/quote/pse/{symbol}/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "en-US,en;q=0.9",
    }
    response = requests.get(url, headers=headers)
    html_response = response.text
    soup = BeautifulSoup(html_response, 'html.parser')
    news = soup.find_all('div', class_='gap-4 border-gray-300 bg-default p-4 shadow last:pb-1 last:shadow-none dark:border-dark-600 sm:border-b sm:px-0 sm:shadow-none sm:last:border-b-0 lg:gap-5 sm:grid sm:grid-cols-news sm:py-6')[0].text
    
    return news

stock = 'bpi'
test = get_news(stock)

pprint.pprint(test)
