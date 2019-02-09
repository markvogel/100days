# https://www.practicepython.org/exercise/2017/02/28/35-birthday-months.html

from collections import Counter
import json

with open("info.json", "r") as f:
    info = json.load(f)

m = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September',
     10: 'October', 11: 'Novemeber', 12: 'December'}

a = Counter([m.get(int(i[:2])) for i in info.values()])
print(a.items())
months = [_ for _ in a.keys()]
counts = [_ for _ in a.values()]
print(months, counts)
# print(json.dumps(a, sort_keys=True, indent=4))
