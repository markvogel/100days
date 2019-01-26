# https://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html

import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'


def get_html(url_input: str):
    r = requests.get(url_input)
    r_html = r.text
    return r_html


def get_paragraphs(html_input: str):
    soup = BeautifulSoup(html_input, 'lxml')
    paragraphs = soup.findAll('p')
    return paragraphs


if __name__ == '__main__':
    # soup = BeautifulSoup(get_html(url))
    # print(soup.prettify())
    # print(get_paragraphs(get_html(url)))
    full_article = []
    for title in get_paragraphs(get_html(url)):
        full_article.append(title.text.replace("\n", " ").strip())
    full_article_text = ' '.join(full_article)
    text_file = open("Output.txt", "w")
    text_file.write(full_article_text)
    text_file.close()
    # for i in full_article:
    #     full = ' '.join(i)
    # print(full)
