def sym(*args):
    new_list = []
    for arg in args:
        if arg == args[-1]:
            break
        for i in arg:
            if i not in args[args.index(arg) + 1]:
                new_list.append(i)
    return new_list


if __name__ == '__main__':
    pass
    # print(sym([1, 2, 3], [5, 2, 1, 4]))
