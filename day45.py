# https://codecombat.com/play/level/magic-exam?

# Try to get the best grade (gold) at the magic exam.
# Move to each X mark, then use a spell.


def action():
    friend = hero.findNearestFriend()
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if friend:
        target = friend
        if target.type == 'soldier':
            hero.cast('heal', target)
        if target.type == 'goliath':
            hero.cast("grow", target)
        if target.type == 'paladin':
            hero.cast("regen", target)
    if enemy:
        target = enemy
        if target.type == 'ogre':
            hero.cast("force-bolt", target)
        if target.type == 'brawler':
            hero.cast("shrink", target)
        if target.type == "scout":
            hero.cast("poison-cloud", target)
    if item:
        target = item


hero.moveXY(18, 40)
action()
hero.moveXY(18, 24)
action()
hero.moveXY(34, 40)
action()
hero.moveXY(34, 24)
action()
hero.moveXY(50, 40)
action()
hero.moveXY(50, 24)
action()
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
        hero.cast("grow", hero)
        pos = item.pos
        x = pos.x
        y = pos.y
        hero.moveXY(x, y)
