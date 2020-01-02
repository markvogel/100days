from under100.day65 import test
import re


def convert_to_decimal(a_list):
    return [(float(i[:-1]) * .01) for i in a_list]


def split_code(a_str):
    for i in range(len(a_str)):
        if a_str[i].isnumeric():
            return [a_str[:i], int(a_str[i:])]


def sub_reddit(a_str):
    return a_str.split(sep='/')[-2]


def test_suite():
    test(convert_to_decimal(["1%", "2%", "3%"]) == [0.01, 0.02, 0.03])
    test(convert_to_decimal(["45%", "32%", "97%", "33%"]) == [0.45, 0.32, 0.97, 0.33])
    test(convert_to_decimal(["33%", "98.1%", "56.44%", "100%"]) == [0.33, 0.981, 0.5644, 1])
    test(split_code("TEWA8392") == ["TEWA", 8392])
    test(split_code("MMU778") == ["MMU", 778])
    test(split_code("SRPE5532") == ["SRPE", 5532])
    test((split_code("SKU8977") == ["SKU", 8977]))
    test((split_code("MCI5589") == ["MCI", 5589]))
    test((split_code("WIEB3921") == ["WIEB", 3921]))
    test(sub_reddit("https://www.reddit.com/r/relationships/") == "relationships")
    test(sub_reddit("https://www.reddit.com/r/mildlyinteresting/") == "mildlyinteresting")
    test(sub_reddit("https://www.reddit.com/r/funny/") == "funny")
    test(sub_reddit("https://www.reddit.com/r/CrappyDesign/") == "CrappyDesign")
    test(sub_reddit("https://www.reddit.com/r/confession/") == "confession")
    test(sub_reddit("https://www.reddit.com/r/AskMen/") == "AskMen")
    test(sub_reddit("https://www.reddit.com/r/comics/") == "comics")
    test(sub_reddit("https://www.reddit.com/r/lifehacks/") == "lifehacks")
    test(sub_reddit("https://www.reddit.com/r/wholesomememes/") == "wholesomememes")
    test(sub_reddit("https://www.reddit.com/r/iamverysmart/") == "iamverysmart")
    test(sub_reddit("https://www.reddit.com/r/starterpacks/") == "starterpacks")
    test(sub_reddit("https://www.reddit.com/r/awww/") == "awww")


if __name__ == '__main__':
    test_suite()
