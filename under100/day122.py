from under100.day65 import test

ROMAN = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def convert_numeral(letter):
    return ROMAN.get(letter)


def roman_numerals(arg):
    if type(arg) == str:
        if len(arg) == 1:
            return convert_numeral(arg)
        end = arg[-1]
        if end in "VXLCDM":  # ["V", "X", "L", "C", "D", "M"]:
            return convert_numeral(end) - sum([ROMAN.get(i) for i in arg[:-1]])
        return sum([ROMAN.get(i) for i in arg])
    if type(arg) == int:
        pass


def test_suite():
    test(roman_numerals("V") == 5)
    test(roman_numerals("IV") == 4)
    test(roman_numerals("CII") == 102)
    test(roman_numerals(45) == "XLV")
    test(roman_numerals(1666) == "MDCLXVI")


if __name__ == '__main__':
    test_suite()
