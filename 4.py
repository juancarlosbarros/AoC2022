"""
AOC2022
Day4
"""

# Part 1
datas = open('4.txt')
sets = []
for line in datas:
    set12 = line.strip().split(",")
    sets.append([int(set12[0].split("-")[0]), int(set12[0].split("-")[1]), int(set12[1].split("-")[0]), int(set12[1].split("-")[1])])
total = 0
"""for set12 in sets:
    set1 = set(range(set12[0], set12[1]))
    set2 = set(range(set12[2], set12[3]))
    if set1 | set2 == set1 or set1 | set2 == set2:
        total += 1
"""
for set12 in sets:
    set2_in_set1 = set12[0] <= set12[2] and set12[1] >= set12[3]
    set1_in_set2 = set12[0] >= set12[2] and set12[1] <= set12[3]
    if set1_in_set2 or set2_in_set1:
        total += 1

print("Part 1")
print(total)

# Part 2
total = 0
for set12 in sets:
    overlap1 = set12[0] >= set12[2] and set12[0] <= set12[3]
    overlap2 = set12[2] >= set12[0] and set12[2] <= set12[1]
    if overlap1 or overlap2:
        total += 1

print("Part 2")
print(total)
