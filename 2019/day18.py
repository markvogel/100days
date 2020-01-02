# https://adventofcode.com/2018/day/2

from input2 import input_list

test = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']

twos = []
threes = []
for i in test:
    print('a ' + str(i.count('a')))
    #
    # if i.count(character) == 2:
    #     twos.append(i)
    # if i.count(character) == 3:
    #     threes.append(i)

print(len(twos))
print(len(threes))
any()
