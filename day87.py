from day65 import test


# TODO just started this challenge - needs finished
# https://edabit.com/challenge/oFwoAA62gRvX5agEN

def test_suite():
    items = [
        {'name': "desk lamp", 'weight': 2, 'value': 12},
        {'name': "beach towel", 'weight': 1, 'value': 10},
        {'name': "textbook", 'weight': 3, 'value': 20},
        {'name': "wall clock", 'weight': 2, 'value': 15},
        {'name': "frozen dinners", 'weight': 10, 'value': 50},
        {'name': "tablet", 'weight': 7, 'value': 1400},
        {'name': "smartphone", 'weight': 1, 'value': 200},
        {'name': "paper", 'weight': 2, 'value': 5},
        {'name': "laser printer", 'weight': 25, 'value': 400},
        {'name': "shoes", 'weight': 1, 'value': 79},
        {'name': "medicine", 'weight': 1, 'value': 17},
        {'name': "decorative cushion", 'weight': 1, 'value': 11},
        {'name': "gold necklace", 'weight': 1, 'value': 2500},
        {'name': "toaster oven", 'weight': 5, 'value': 129}
    ]
    test(knapsack(0, items) == {
        'capacity': 0,
        'items': [],
        'weight': 0,
        'value': 0
    })
    test(knapsack(1, items) == {
        'capacity': 1,
        'items': [
            {'name': "gold necklace", 'weight': 1, 'value': 2500}
        ],
        'weight': 1,
        'value': 2500
    })
    test(knapsack(2, items) == {
        'capacity': 2,
        'items': [
            {'name': "smartphone", 'weight': 1, 'value': 200},
            {'name': "gold necklace", 'weight': 1, 'value': 2500}
        ],
        'weight': 2,
        'value': 2700
    })
    test(knapsack(5, items) == {
        'capacity': 5,
        'items': [
            {'name': "smartphone", 'weight': 1, 'value': 200},
            {'name': "shoes", 'weight': 1, 'value': 79},
            {'name': "medicine", 'weight': 1, 'value': 17},
            {'name': "decorative cushion", 'weight': 1, 'value': 11},
            {'name': "gold necklace", 'weight': 1, 'value': 2500}
        ],
        'weight': 5,
        'value': 2807
    })
    test(knapsack(14, items) == {
        'capacity': 14,
        'items': [
            {'name': "tablet", 'weight': 7, 'value': 1400},
            {'name': "smartphone", 'weight': 1, 'value': 200},
            {'name': "gold necklace", 'weight': 1, 'value': 2500},
            {'name': "toaster oven", 'weight': 5, 'value': 129}
        ],
        'weight': 14,
        'value': 4229
    })

    test(highest_value_item(items) == {'name': "gold necklace", 'weight': 1, 'value': 2500})


def knapsack(max_weight: int, items: list):
    k_items = []
    weight, value = 0, 0

    return {"capacity": max_weight,
            "items": [],
            "weight": weight,
            "value": value
            }


def highest_value_item(items: list):
    highest_value = items[0].get("value") / items[0].get("weight")
    item = items[0]
    for i in items:
        item_value = i.get("value") / i.get("weight")
        if item_value > highest_value:
            highest_value = item_value
            item = i
    return item


def add_item(a_list, a_item):
    return a_list.append(a_item)


if __name__ == '__main__':
    test_suite()
