# https://www.py4e.com/html3/12-network
import socket
import ssl
import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup


# Exercise 3
def getpage(webpage="http://data.pr4e.org/romeo.txt"):
    try:
        response = urllib.request.urlopen(webpage)
        html = response.read()

    except:
        print("you entered an invalid url ")
        exit()
    print(html.decode("utf-8")[:2999])
    print(len(html))


# Code: http://www.py4e.com/code3/socket1.py


def get_page():
    return input("Please enter a webpage: ")


# exercise4
def urllinks():
    # To run this, you can install BeautifulSoup
    # https://pypi.python.org/pypi/beautifulsoup4

    # Or download the file
    # http://www.py4e.com/code3/bs4.zip
    # and unzip it in the same directory as this file

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter - ')
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('p')
    print(f"There are {len(tags)} paragraph tags on the site {url}")

    # for tag in tags:
    #     print(tag.get('href', None))

    # Code: http://www.py4e.com/code3/urllinks.py


# exercise5
def socket1(webpage="http://data.pr4e.org/romeo.txt"):
    total_text = ""
    try:
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mysock.connect((webpage.split(sep="/")[2], 80))
        cmd = f"GET {webpage} HTTP/1.0\r\n\r\n".encode()
        mysock.send(cmd)

        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            text = data.decode()
            total_text += text
        mysock.close()

    except TabError:
        print("you entered an invalid url ")
        exit()
    printed_text = ""
    for c, l in enumerate(total_text):
        if c < 3000:
            printed_text += l
    # print(printed_text)
    test = total_text.split(sep="\r")
    print(test[-1])

    # print(len(total_text))


if __name__ == '__main__':
    socket1()
