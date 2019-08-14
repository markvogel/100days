def elev():
    usf = input('Enter the US Floor Number: ')
    wf = int(usf) - 1
    print('Non-US Floor Number is',wf)

    # Code: http://www.py4e.com/code3/elev.py


def urllinks():
    # To run this, you can install BeautifulSoup
    # https://pypi.python.org/pypi/beautifulsoup4

    # Or download the file
    # http://www.py4e.com/code3/bs4.zip
    # and unzip it in the same directory as this file

    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup
    import ssl

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


class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

    def party2(self):
        self.x = self.x -1
        print("So far", self.x)

    # Code: http://www.py4e.com/code3/party2.py


if __name__ == '__main__':
    an = PartyAnimal()
    an.party()
    an.party()
    an.party()
    PartyAnimal.party(an)
