def party1():
    stuff = list()
    stuff.append('python')
    stuff.append('chuck')
    stuff.sort()
    print(stuff[0])
    print(stuff.__getitem__(0))
    print(list.__getitem__(stuff, 0))
    print(list.__getitem__(stuff, 1))

    # Code: http://www.py4e.com/code3/party1.py


def elev():
    usf = input('Enter the US Floor Number: ')
    wf = int(usf) - 1
    print('Non-US Floor Number is', wf)

    # Code: http://www.py4e.com/code3/elev.py


def urllinks():
    # To run this, you can install BeautifulSoup
    # https://pypi.python.org/pypi/beautifulsoup4

    # Or download the file
    # http://www.py4e.com/code3/bs4.zip
    # and unzip it in the same directory as this file

    import urllib.request, urllib.error
    from bs4 import BeautifulSoup
    import ssl
    try:

        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        url = input('Enter - ')
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')

        # Retrieve all of the anchor tags
        tags = soup('a')
        for tag in tags:
            print(tag.get('href', None))

        # Code: http://www.py4e.com/code3/urllinks.py
    except ValueError:
        print("You entered an invalid url, please try again... ")
        urllinks()


if __name__ == '__main__':
    urllinks()
