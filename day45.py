# https://codecombat.com/play/level/magic-exam?

# Try to get the best grade (gold) at the magic exam.
# Move to each X mark, then use a spell.

hero.moveXY(18, 40)
hero.cast("heal", hero.findNearestFriend())
hero.moveXY(18, 24)
hero.cast("force-bolt", hero.findNearestEnemy())
hero.moveXY(34, 40)
hero.cast("grow", hero.findNearestFriend())
hero.moveXY(34, 24)
hero.cast("shrink", hero.findNearestEnemy())
hero.moveXY(50, 40)
hero.cast("regen", hero.findNearestFriend())
hero.moveXY(50, 24)
hero.cast("poison-cloud", hero.findNearestEnemy())
hero.moveXY(66, 40)
find_item()
hero.moveXY(66, 24)
find_item()


def find_item():
    item = hero.findNearestItem()
    if item.type == 'potion':
        # Move to the position of the item.
        pos = item.pos
        x = pos.x
        y = pos.y
        hero.moveXY(x, y)
    if item.type == 'poison':
        # Move to the position of the item.
        hero.cast("regen", hero)
        pos = item.pos
        x = pos.x
        y = pos.y
        hero.say("poison")
