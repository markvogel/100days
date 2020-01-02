class PartyAnimal:
    x = 0

    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


class ProgrammingIsFun:
    x = ""

    def program(self):
        x = 1
        self.x = self.x + "a"
        print(self.x, x)


class PartyAnimal4:
    x = 0

    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)

    def __del__(self):
        print('I am destructed', self.x)


# Code: http://www.py4e.com/code3/party4.py

class PartyAnimal5:
    x = 0
    name = ''

    def __init__(self, nam):
        self.name = nam
        print(self.name, 'constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, 'party count', self.x)


# Code: http://www.py4e.com/code3/party5.py

if __name__ == '__main__':
    # an = PartyAnimal()
    # an.party()
    # an.party()
    # an.party()
    # PartyAnimal.party(an)

    # Code: http://www.py4e.com/code3/party2.py

    # b = ProgrammingIsFun()
    # b.program()
    # b.program()
    # ProgrammingIsFun.program(b)

    # an = PartyAnimal()
    # print("Type", type(an))
    # print("Dir ", dir(an))
    # print("Type", type(an.x))
    # print("Type", type(an.party))

    # an = PartyAnimal4()
    # an.party()
    # an.party()
    # an = 42
    # print('an contains', an)

    s = PartyAnimal5('Sally')
    j = PartyAnimal5('Jim')

    s.party()
    j.party()
    s.party()
