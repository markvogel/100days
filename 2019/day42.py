# want to print out the matching list values if they are similar to other list values

from pprint import pprint as p
import difflib

some_list = ['S123', 'abcdefgh', '123abc', '333abc', '123459', '1111', 'afdafdsjklfjlkasdjabc', '11111', '1111111',
             'def', 'defg', 'abcdef']

# matching = [difflib.get_close_matches(s, some_list) for s in some_list if
#             (len(difflib.get_close_matches(s, some_list)) > 1)]

matching = []
for s in some_list:
    test = sorted(difflib.get_close_matches(s, some_list))
    if len(test) > 1:
        if test not in matching:
            matching.append(test)

p(matching)
print(len(matching))
