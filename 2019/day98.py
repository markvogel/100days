from under100.day65 import test


def no_odds(a_list):
    return [i for i in a_list if not i % 2]


def cap_me(a_list):
    return [i.title() for i in a_list]


def is_parsel_tongue(sentence):
    s_list = sentence.split()
    for i in s_list:
        i = i.lower()
        if i.count("s") == 1:
            return False
        if i.count("s") == 2 and i.startswith("s") and i.endswith("s"):
            return False
    return True


def test_suite():
    test(no_odds([1, 2, 3, 4, 5, 6, 7, 8]) == [2, 4, 6, 8])
    test(no_odds([43, 65, 23, 89, 53, 9, 6]) == [6])
    test(no_odds([718, 991, 449, 644, 380, 440]) == [718, 644, 380, 440])
    test(cap_me(["mavis", "senaida", "letty"]) == ["Mavis", "Senaida", "Letty"])
    test(cap_me(["samuel", "MABELLE", "letitia", "meridith"]) == ["Samuel", "Mabelle", "Letitia", "Meridith"])
    test(cap_me(["Slyvia", "Kristal", "Sharilyn", "Calista"]) == ["Slyvia", "Kristal", "Sharilyn", "Calista"])
    test(is_parsel_tongue("Sshe ssselects to eat that apple. "))
    test(not is_parsel_tongue("She ssselects to eat that apple. "))
    # // "She" only contains one s.
    test(is_parsel_tongue("You ssseldom sssspeak sso boldly, ssso messmerizingly."))
    test(is_parsel_tongue("Sshe ssselects to eat that apple."))
    test(not is_parsel_tongue("She ssselects to eat that apple."))
    test(is_parsel_tongue("You ssseldom sssspeak sso boldly, ssso messmerizingly."))
    test(not is_parsel_tongue("Steve likes to eat pancakes"))
    test(is_parsel_tongue("Sssteve likess to eat pancakess"))
    test(not is_parsel_tongue("Beatrice samples lemonade"))
    test(is_parsel_tongue("Beatrice enjoysss lemonade"))


if __name__ == '__main__':
    test_suite()
