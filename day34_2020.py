nade = open('nade.txt', 'r')
# aw = open('aw_tc75.txt', 'r')

# print(read_file.read().split(sep="No attendance record found for this Sale Type/Bidder Number.")[2])

lines = (nade.readlines())
# lines2 = (aw.readlines())
for c, line in enumerate(lines):
    hostname = line.split()[0]
    # print(hostname)
    num = 10
    if hostname.endswith("LT") or hostname.endswith("DT"):
        continue
    if len(hostname[5:]) == num:
        print(hostname)