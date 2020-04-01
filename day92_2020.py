if __name__ == '__main__':
    with open("employees.txt") as f:
        dlist = f.readlines()
    for i in dlist:
        print('.'.join(i.strip().split()) + "@domain.com")
