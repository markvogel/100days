from under100.day65 import test


# https://edabit.com/challenge/D69v5RSgzFPqsyfwf
def spelling(a_str):
    new_str = []
    for i in range(len(a_str)):
        new_str.append(a_str[:i + 1])
    print(new_str)
    return new_str


def test_suite():
    test(spelling("bee") == ["b", "be", "bee"])
    test(spelling("happy") == ["h", "ha", "hap", "happ", "happy"])
    test(spelling("eagerly") == ["e", "ea", "eag", "eage", "eager", "eagerl", "eagerly"])


if __name__ == '__main__':
    test_suite()
