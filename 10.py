"""
AOC2022
Day10
"""

datas = open('10.txt')
instructions = datas.readlines()

# Part 1
stack = [1] # value AFTER n cycles

for inst in instructions:
    inst = inst.strip().split()
    last = stack[-1]
    stack.append(last)
    if inst[0] == "addx":
        stack.append(last + int(inst[1]))

def calcul(cycles):
    total = 0
    for c in cycles:
        # print(c, stack[c-1])
        total += c * stack[c-1]
    return total

print("Part1:")
print(calcul([20, 60, 100, 140, 180, 220]))

# Part2
CRT = ["."] * 240
for cycle in range(240):
    if cycle%40-1 <= stack[cycle] <= cycle%40+1:
        CRT[cycle] = "#"
print("Part2")        
for i in range(240):
    if i%40 == 39:
        print(CRT[i])
    else:
        print(CRT[i], end="")
