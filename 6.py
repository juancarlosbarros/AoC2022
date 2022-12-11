"""
AOC2022
Day6
"""

# Part 1
datas = open('6.txt')
txt = datas.read()
for i in range(3, len(txt)):
    if len(set(txt[i-3:i+1])) == 4:
        break
print("Part1")
print(i+1, txt[i-3:i+1])

# Part 2
for i in range(13, len(txt)):
    if len(set(txt[i-13:i+1])) == 14:
        break
print("Part2")
print(i+1, txt[i-13:i+1])