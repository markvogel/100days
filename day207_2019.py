class PartyAnimal5:
    x = 0
    name = ''

    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)


class CricketFan(PartyAnimal5):
    points = 0

    def six(self):
        self.points = self.points + 6
        self.party()
        print(self.name, "points", self.points)


if __name__ == '__main__':
    s = PartyAnimal5("Sally")
    s.party()
    j = CricketFan("Jim")
    j.party()
    j.six()
    print(dir(j))

# Code: http://www.py4e.com/code3/party6.py
list()
