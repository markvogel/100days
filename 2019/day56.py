def check(a: str):
    if 'ei' in a:
        a = a.split(sep='ei')
        if a[0][-1] == 'c':
            return True
        return False
    if 'ie' in a:
        a = a.split(sep='ie')
        if a[0][-1] == 'c':
            return False
    return True


if __name__ == '__main__':
    print(check('a'))
    print(check('zombie'))
    print(check('transceiver'))
    print(check('veil'))
    print(check('icier'))
