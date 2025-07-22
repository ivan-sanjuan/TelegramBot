from bs4 import BeautifulSoup
import requests

def get_stats(symbol):
    url = f'https://stockanalysis.com/quote/pse/{symbol}/statistics/'
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html,'html.parser')
    stats = {}
    valuation_column = soup.find_all('table', class_='w-full')[3]
    pe_ratio = None
    for row in valuation_column.find_all('tr', class_='border-y border-gray-200 odd:bg-gray-50 dark:border-dark-700 dark:odd:bg-dark-775'):
        if 'PE Ratio' in row.text:
            result_pe = row.text
            pe_ratio = result_pe.split()[2]
    ps_ratio = None        
    for row in valuation_column.find_all('tr', class_='border-y border-gray-200 odd:bg-gray-50 dark:border-dark-700 dark:odd:bg-dark-775'):
        if 'PS Ratio' in row.text:
            result_ps = row.text
            ps_ratio = result_ps.split()[2]
    peg_ratio = None        
    for row in valuation_column.find_all('tr', class_='border-y border-gray-200 odd:bg-gray-50 dark:border-dark-700 dark:odd:bg-dark-775'):
        if 'PEG Ratio' in row.text:
            result_peg = row.text
            peg_ratio = result_peg.split()[2]

    efficiency_column = soup.find_all('table', class_='w-full')[6]
    roe = None
    for row in efficiency_column.find_all('tr', class_='border-y border-gray-200 odd:bg-gray-50 dark:border-dark-700 dark:odd:bg-dark-775'):
        if 'Return on Equity (ROE)' in row.text:
            result_roe = row.text
            roe = result_roe.split()[4]
            
    stats['PE Ratio'] = pe_ratio
    stats['PS Ratio'] = ps_ratio
    stats['PEG Ratio'] = peg_ratio
    stats['Return on Equity'] = roe
    
    return stats