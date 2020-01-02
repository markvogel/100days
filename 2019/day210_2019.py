# day210


if __name__ == '__main__':
    stuff = list()
    stuff.append('python')
    stuff.append('apple')
    stuff.sort()
    print(len(stuff))
    print(stuff[0])
    print(stuff[1])
    print(stuff.__getitem__(0))
    print(stuff.__getitem__(1))
    print(list.__getitem__(stuff, 0))
    print(list.__getitem__(stuff, 1))
