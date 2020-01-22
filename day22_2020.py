read_file = open('blockclient.log', 'r')

# print(read_file.read().split(sep="No attendance record found for this Sale Type/Bidder Number.")[2])

lines = (read_file.readlines())
for c, line in enumerate(lines):
    if "sell run:" in line or "Offering sale" in line:
        print(line[-68:], end="")
