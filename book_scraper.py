from bs4 import BeautifulSoup
import requests
import urllib.parse

def search_book(data):
    book_name = urllib.parse.quote(data)
    url = f'https://z-library.sk/s/{book_name}'
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    html_data = response.text
    soup = BeautifulSoup(html_data, 'html.parser')
    trimmed_soup = soup.find_all('div', id='searchResultBox')[0]
    book_results = trimmed_soup.find_all('div', class_='book-item resItemBoxBooks')
    book_list = []
    index = 0
    max_results = 10
    results = book_results
    while len(book_list) < max_results and index < len(results):
        books = results[index]
        card = books.find('z-bookcard')
        if card:
            language = card.get('language')
            extension = card.get('extension')
            if language == 'English' and extension == 'epub':
                title = card.find('div', {'slot': 'title'}).text.strip() or 'N/A'
                author = card.find('div', {'slot': 'author'}).text.strip()  or 'N/A'
                filesize = card.get('filesize') or 'N/A'
                dl_link = card.get('href') or 'N/A'
                
                book_dict = {
                'Title': title,
                'Author': author,
                'Language': language,
                'Ext.': extension,
                'Filesize': filesize,
                'Download Link': dl_link
                }

                book_list.append(book_dict)
        index += 1

    return book_list

