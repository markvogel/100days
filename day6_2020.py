players = """SEAN - LEBIRO
KEVIN - OPP
SMITTY - SETTING 
COREY - OH, MIDDLE
MARK - OH, MIDDLE 
JESSE - OH
TYLER - MIDDLE
BILL - MIDDLE 
BRETT - MIDDLE, OH
ANDRES - OH, OPP
JERRY - MIDDLE
JOSH - MIDDLE, OPP"""

p = players.split(sep="\n")
names = [i.split(sep="-") for i in p]

print(p)
print(names)
for i in names:
    print(i[1])
