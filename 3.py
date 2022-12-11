from collections import Counter
"""
AOC2022
Day3
"""
# Part 1
sacs = open('3.txt')
repeated = []
for sac in sacs:
    sac = sac.strip()
    mid = len(sac)//2
    sac1 = sac[:mid]
    sac2 = sac[mid:]
    set1 = set(sac1)
    set2 = set(sac2)
    item = set1 & set2
    repeated.extend(item)
counter_repeated = Counter(repeated)
total = 0
for key, value in counter_repeated.items():
    if key in "QWERTZUIOPASDFGHJKLYXCVBNM":
        total += value*(ord(key)-ord('A') + 27)
    if key in "qwertzuiopasdfghjklyxcvbnm":
        total += value*(ord(key)-ord('a') + 1)
print("Part 1")
print(total)
# print(repeated)
# print(counter_repeated)

# Part 2
f = open('3.txt')
sacs = []
Nb_sacs = 0
for sac in f:
    sac = sac.strip()
    sacs.append(sac)
groups = []
for i in range(100):
    sac1 = sacs[3*i]
    sac2 = sacs[3*i+1]
    sac3 = sacs[3*i+2]
    group = set(sac1) & set(sac2) & set(sac3)
    groups.extend(list(group))
print(groups)

total = 0
for value in groups:
    if value in "QWERTZUIOPASDFGHJKLYXCVBNM":
        total += ord(value)-ord('A') + 27
    if value in "qwertzuiopasdfghjklyxcvbnm":
        total += ord(value)-ord('a') + 1
print("Part 2")
print(total)

