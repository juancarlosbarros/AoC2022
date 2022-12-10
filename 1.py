"""
AOC2022
Day1
"""
f = open('1.txt')
calories = []
total = 0
for line in f:
    if line == "\n":
        calories.append(total)
        total = 0
    else:
        total += int(line)
print(sum(sorted(calories)[-3:]))
        