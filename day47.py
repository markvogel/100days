# https://www.reddit.com/r/dailyprogrammer/comments/afxxca/20190114_challenge_372_easy_perfectly_balanced/

def balanced(a: str):
    xs, ys, = a.count('x'), a.count('y')
    if xs == ys:
        return True
    return False


def balanced_bonus(b: str):
    bonus = [i for i in b]
    bonus_set = set(bonus)
    new = set([bonus.count(each) for each in bonus_set])
    # new = set(new)
    if len(new) > 1:
        return False
    return True


if __name__ == '__main__':
    print(balanced("xxxyyy"))
    print(balanced("yyyxxx"))
    print(balanced("xxxyyyy"))
    print(balanced("yyxyxxyxxyyyyxxxyxyx"))
    print(balanced("xyxxxxyyyxyxxyxxyy"))
    print(balanced(""))
    print(balanced("x"))
    print('\n')
    print(balanced_bonus("xxxyyyzzz"))
    print(balanced_bonus("abccbaabccba"))
    print(balanced_bonus("xxxyyyzzzz"))
    print(balanced_bonus("abcdefghijklmnopqrstuvwxyz"))
    print(balanced_bonus("pqq"))
    print(balanced_bonus("fdedfdeffeddefeeeefddf"))
    print(balanced_bonus("www"))
    print(balanced_bonus("x"))
    print(balanced_bonus(""))
