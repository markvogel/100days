snow = open('snow_tc75.txt', 'r')
aw = open('aw_tc75.txt', 'r')

# print(read_file.read().split(sep="No attendance record found for this Sale Type/Bidder Number.")[2])

lines = (snow.readlines())
lines2 = (aw.readlines())
for c, line in enumerate(lines):
    if line[1:] not in lines2:
        print(line[1:])