import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
from prettytable import PrettyTable
import requests
import pprint
import csv

def search_div(symbol):
    url = f'https://stockanalysis.com/quote/pse/{symbol}/dividend/'
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9",
    }
    response = requests.get(url, headers=headers)
    html_data = response.text
    soup = BeautifulSoup(html_data,'html.parser')
    div_table = soup.find('div', class_='mt-4 bp:mt-7')
    rows = div_table.find_all('tr')
    with open('dividend_history.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        table = PrettyTable()
        for row in rows:
            table.cols = row.find_all(['th', 'td'])
            table.data = [col.get_text(strip=True) for col in table.cols]
            writer.writerow(table.data)
    div_df = pd.read_csv('dividend_history.csv', index_col=None, na_values=['N/A'])
    
    return div_df