def mk_list(a_str):
    return a_str.split(sep=",")


def opcode(a_list):
    a = a_list
    if a[0] == "99":
        return
    if a[0] == "1":
        a[int(a[int(3)])] = foo(a, 1) + foo(a, 2)
    if a[0] == "2":
        a[int(a[int(3)])] = foo(a, 1) * foo(a, 2)
    return a


def foo(a_list, i):
    return int(a_list[int(a_list[int(i)])])


if __name__ == '__main__':
    sample = "1,9,10,3,2,3,11,0,99,30,40,50"
    print(opcode(mk_list(sample)))
