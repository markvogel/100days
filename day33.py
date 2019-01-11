# https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'


def get_html(url_input: str):
    r = requests.get(url_input)
    r_html = r.text
    return r_html


def get_titles(html_input: str):
    soup = BeautifulSoup(html_input, 'lxml')
    titles = soup.findAll('h2')
    return titles


if __name__ == '__main__':
    # soup = BeautifulSoup(get_html(url))
    # print(soup.prettify())
    # print(get_paragraphs(get_html(url)))
    for title in get_titles(get_html(url)):
        if 'Site' not in title.text:
            print(title.text)
