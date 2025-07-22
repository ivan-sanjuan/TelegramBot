from bs4 import BeautifulSoup
import requests
import pprint

stock_symbol = 'BPI'
url = f'https://stockanalysis.com/quote/pse/{stock_symbol}/financials/ratios/'
response = requests.get(url)
html_response = response.text
soup = BeautifulSoup(html_response, 'html.parser')

financial_table = soup.find('div', id='main-table-wrap')


def get_metrics():
    for row in financial_table.find_all('th', id='TTM'):
        for period in row.find_all('span', class_='hidden sm:inline'):
            period = row.text
            full_date = period.split(' ', 2)[2]

    pe_ratio = None
    for row in financial_table.find_all('tr'):
        if 'PE Ratio' in row.text:
            pe_ratio = row
            break
    pe_ratio_2025 = [td.text.strip() for td in pe_ratio.find_all('td')][1]
    
    ps_ratio = None
    for row in financial_table.find_all('tr'):
        if 'PS Ratio' in row.text:
            ps_ratio = row
            break
    ps_ratio_2025 = [td.text.strip() for td in ps_ratio.find_all('td')][1]

    for row in financial_table.find_all('tr'):
        if 'Last Close Price' in row.text:
            last_closing = row
            break
    last_closing_2025 = [td.text.strip() for td in last_closing.find_all('td')][1]
    
    ratio_and_metrics = {}
    ratio_and_metrics['Date:'] = full_date
    ratio_and_metrics['PE Ratio:'] = pe_ratio_2025
    ratio_and_metrics['PS Ratio:'] = ps_ratio_2025
    ratio_and_metrics['Last Closing Price:'] = last_closing_2025
    
    return ratio_and_metrics
    
values = get_metrics()

pprint.pprint(values)