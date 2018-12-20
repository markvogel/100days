# reverse a string - when using brackets, [start:stop:step]

test_string = 'test-string'
new = test_string[::-1]
print(new)

# wanted to do it differently
new_string = ''
for i in range(1, len(test_string) + 1):
    new_string += test_string[-i]

print(new_string)
