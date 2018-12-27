# comparing sets

a = [1, 2, 3, 4, 5]
b = [9, 8, 7, 6, 5]

# exists in both lists
both = set(a).intersection(b)
# exists only in a
a_only = set(a) - set(b)
# exists only in b
b_only = set(b) - set(a)

print(both, a_only, b_only)
