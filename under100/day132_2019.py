from under100.day65 import test

V = "AEIOU"


# https://www.hackerrank.com/challenges/the-minion-game/problem
def minion_game(a):
    global s, k
    s, k = 0, 0
    for i in range(len(a)):
        if a[i] in V:
            k += a.count(a[i])
            new_string = str(a[i:])
            stuart_score(new_string, s)
            break
        if a[i] not in V:
            s += a.count(a[i])
            new_string = a[i:]
            kevin_score(new_string, k)
            break

    if s == k:
        print("Draw")
        return None
    if s > k:
        print(f"Stuart {s}")
        return f"Stuart {s}"
    if s < k:
        print(f"Kevin {k}")
        return f"Kevin {k}"


def stuart_score(str1, s):
    for i in range(len(str1)):
        s += str1.count(str1[i:])
    return s


def kevin_score(str2, k):
    for i in range(len(str2)):
        k += str2.count(str2[i:])
    return k


def test_suite():
    test(minion_game("BANANA") == "Stuart 12")


if __name__ == '__main__':
    test_suite()
    minion_game("A")
