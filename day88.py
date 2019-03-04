from day65 import test


def phone_digit(a: str = None):
    phone_digits = {'a': 2, 'b': 2, 'c': 2,
                    'd': 3, 'e': 3, 'f': 3,
                    'g': 4, 'h': 4, 'i': 4,
                    'j': 5, 'k': 5, 'l': 5,
                    'm': 6, 'n': 6, 'o': 6,
                    'p': 7, 'q': 7, 'r': 7, 's': 7,
                    't': 8, 'u': 8, 'v': 8,
                    'w': 9, 'x': 9, 'y': 9, 'z': 9}
    if a in phone_digits:
        return phone_digits.get(a)


# https://edabit.com/challenge/nh3daaT8LHbv8mKXA
def text_to_num(a_str):
    temp = ''
    for i in a_str:
        i = i.lower()
        if i.isalpha():
            a = phone_digit(i)
            temp += str(a)
            continue
        temp += i
    return temp


# https://edabit.com/challenge/ic9aKYukaRH2MjDyk
def sort_by_last(a_str):
    a_list = a_str.split()
    reversed_str_list = [i[::-1] for i in a_list]
    sorted_by_last_char = sorted(reversed_str_list)
    fixed_list = [i[::-1] for i in sorted_by_last_char]
    fixed_str = " ".join(fixed_list)
    return fixed_str


# https://edabit.com/challenge/Eou5gLqeXZu5mKjeA
def replace_nth(txt, nth, old_char, new_char):
    count = 0
    new_str = ''
    for i in txt:
        if i == old_char:
            count += 1
            if nth == count:
                new_str += new_char
                count = 0
                continue
        new_str += i
    return new_str


def test_suite():
    test(text_to_num("123-647-EYES") == "123-647-3937")
    test(text_to_num("(325)444-TEST") == "(325)444-8378")
    test(text_to_num("653-TRY-THIS") == "653-879-8447")
    test(text_to_num("435-224-7613") == "435-224-7613")
    test(sort_by_last("herb camera dynamic") == "camera herb dynamic")
    test(sort_by_last("stab traction artist approach") == "stab approach traction artist")
    test(sort_by_last("sample partner autonomy swallow trend") == "trend sample partner swallow autonomy")
    test(replace_nth("Vader said: No, I am your father!", 2, "a", "o") == "Vader soid: No, I am your fother!")
    test(replace_nth("A glittering gem is not enough.", 0, "o", "-") == "A glittering gem is not enough.")


if __name__ == '__main__':
    test_suite()
