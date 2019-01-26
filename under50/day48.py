# https://www.reddit.com/r/dailyprogrammer/comments/98ufvz/20180820_challenge_366_easy_word_funnel_1/


def funnel(a: str, b: str):
    a, b = list(a), list(b)
    for i in range(len(b)):
        try:
            a.remove(b[i])
        except ValueError:
            continue
    if len(a) > 1:
        return False
    return True


if __name__ == '__main__':
    print(funnel("leave", "eave"))
    print(funnel("reset", "rest"))
    print(funnel("dragoon", "dragon"))
    print(funnel("eave", "leave"))
    print(funnel("sleet", "lets"))
    print(funnel("skiff", "ski"))
