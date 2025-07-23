from bs4 import BeautifulSoup
import requests
import urllib.parse



def search_book(book):
    book_name = urllib.parse.quote(book.lower())
    url = f'https://z-library.sk/s/{book_name}'
    response = requests.get(url)
    html_data = response.text
    soup = BeautifulSoup(html_data, 'html.parser')
    trimmed_soup = soup.find_all('div', id='searchResultBox')[0]
    book_results = trimmed_soup.find_all('div', class_='book-item resItemBoxBooks')
    book_list = []
    index = 0
    max_results = 20
    results = book_results
    while index < max_results:
        books = results[index]
        card = books.find('z-bookcard')
        if card:
            title = card.find('div', {'slot': 'title'}).text.strip() or 'N/A'
            author = card.find('div', {'slot': 'author'}).text.strip()  or 'N/A'
            language = card.get('language') or 'N/A'
            extension = card.get('extension') or 'N/A'
            filesize = card.get('filesize') or 'N/A'
            download = card.get('download') or 'N/A'
            
            search_results = (
                f'📚{title.strip()}\n'
                f'by {author.strip()}\n'
                f'Language: {language.strip()}\n'
                f'({extension} ({filesize}))\n'
                f'🔽 https://z-library.sk{download.strip()} 🔽\n\n'
            )
            book_list.append(search_results)
        index += 1
    return book_list