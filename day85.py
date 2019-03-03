from day65 import test


# https://edabit.com/challenge/kBXHbwQZPiLmwjrMy

def divisible(param):
    return not bool(param % 100)


def concat_name(first, last):
    # return "{}, {}".format(last, first)
    return f"{last}, {first}"


def identify(a_str):
    if not len(a_str):
        return a_str

    word_list = make_list(a_str)

    for i in range(len(word_list)):
        if starts_with_vowel(word_list[i]):
            word_list[i] = add_yay(word_list[i])
            break
        if starts_with_vowel(word_list[i]):
            word_list[i] = move_letter_to_end(word_list[i])
    print(" ".join(word_list))
    return " ".join(word_list)


def starts_with_vowel(a_str):
    return a_str[0] in "aeiouy"


def move_letter_to_end(a_str):
    return a_str[1:] + a_str[0]


def add_yay(a_str):
    return a_str + "yay"


def make_list(a_str):
    return a_str.lower().split()


def test_suite():
    # test(not divisible(1))
    # test(divisible(1000))
    # test(divisible(100))
    # test(concat_name("John", "Doe") == "Doe, John")
    # test(concat_name("Mary", "Jane") == "Jane, Mary")
    test(identify("Have") == "avehay")
    test(identify("Cram") == "amcray")
    test(identify("Take") == "aketay")
    test(identify("Cat") == "atcay")
    test(identify("Shrimp") == "impshray")
    test(identify("Trebuchet") == "ebuchettray")
    test(identify("Ate") == "ateyay")
    test(identify("Apple") == "appleyay")
    test(identify("Oaken") == "oakenyay")
    test(identify("Eagle") == "eagleyay")
    test(identify("Ink") == "inkyay")
    test(identify("Unicorn") == "unicornyay")
    test(identify("") == "")
    test(identify("Delirious") == "eliriousday")
    test(identify("I like to eat honey waffles.") == "Iyay ikelay otay eatyay oneyhay afflesway.")
    test(identify("Do you think it is going to rain today?") ==
         "Oday ouyay inkthay ityay isyay oinggay otay ainray odaytay?")
    test(identify("What is the weather today?") == "Atwhay isyay ethay eatherway odaytay?")
    test(identify("Have") == "avehay")
    test(identify("Horde") == "ordehay")


if __name__ == '__main__':
    test_suite()
