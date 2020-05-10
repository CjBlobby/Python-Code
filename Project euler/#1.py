numlist = []
multiple = 0
while multiple < 1000:
    numlist.append(multiple)
    multiple += 3

multiple = 5
while multiple < 1000:
    numlist.append(multiple)
    multiple += 5

total = 0
for num in set(numlist):
    total += num
print(total)
