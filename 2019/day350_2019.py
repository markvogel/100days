if __name__ == '__main__':
    path = 'input.txt'
    file = open(path, 'r')
    f = file.read()
    a = f.split()
    dell = []
    for i in a:
        if i.startswith("84:7B:EB"):
            print(i)
            dell.append(i)
    print(len(dell))
