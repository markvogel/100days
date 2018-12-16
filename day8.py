# I didn't have a strong idea in mind for today, but I wanted to brush up on list comprehensions.  It only took a couple
# of minutes to research and recall.

sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

comprehension = [i + 100 for i in sample_list if i < 11]
print(comprehension)

new_list = []
for i in sample_list:
    new_list.append(i + 100)

print(new_list)

# I regularly need to create ODBC connections on computers in a windows environment.  I'd like to automate this, so I
# did a quick search and found this golden nugget on github:
# https://github.com/ActiveState/code/tree/73b09edc1b9850c557a79296655f140ce5e853db/recipes/Python/414879_Create_an_ODBC_data_source
# I'll need to research more to understand exactly how it works, but this would automate some of the work I do
