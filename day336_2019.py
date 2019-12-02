def mk_list(a_str):
    return a_str.split(sep=",")


def opcode(a_list):
    c = 0
    a = list(a_list)
    if a[0] == "99":
        return a
    if a[0] == "1":
        a[int(a[int(3)])] = foo(a, 1) + foo(a, 2)
    if a[0] == "2":
        print(a[int(a[int(3)])], foo(a, 1), foo(a, 2))
        a[int(a[int(3)])] = foo(a, 1) * foo(a, 2)
    c += 4
    opcode(a[(-len(a) + c):])
    print(opcode(a[(-len(a) + c):]))
    return a


def foo(a_list, i):
    return int(a_list[int(a_list[int(i)])])


if __name__ == '__main__':
    sample = "1,9,10,3,2,3,11,0,99,30,40,50"
    l = mk_list(sample)
    print(opcode(l))
