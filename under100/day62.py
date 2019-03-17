import json

with open("info.json", "r") as f:
    info = json.load(f)

if info["has_a_dog"]:
    print(f'{info["name"]} has a dog')
else:
    print(f'{info["name"]} does not have a dog')
