# normalizing and cleaning list data

sample = ['S1234567890', 's1234567890', '1234567890', 'S123456789', '123456789', 'S1234567891', 'S1234567892']
test_sample = [i.lower() for i in sample]

for s in test_sample:
    if s[0] == 's' and s in test_sample:
        print(s[1:])

for s in test_sample:
    if s[0] != 's' and s in test_sample:
        print(f'exists in list, but doesn\'t start with: {s}')

for s in test_sample:
    if s[0] != 's' and 's' + s in test_sample:
        print(f'exists in list, starting with and without s: {s}')
