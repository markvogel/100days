import datetime

year = datetime.date.today().year

age = input('please enter your age: ')
a = 100 - int(age)
b = year + a
print(f'you will be 100 in the year {b}')
