"""
AOC2022
Day5
"""

# Part 1
datas = open('5.txt')
line = datas.readline()
stacks1 = [[] for _ in range(9)]

while line !="\n":
    for i in range(9):
        index = 4 * i + 1
        carac = line[index]
        if carac.isalpha():
            stacks1[i] = [carac] + stacks1[i]
    line = datas.readline()
    
instructs = datas.readlines()

for line in instructs:
    instruct = line.split()
    combien = int(instruct[1])
    depuis = int(instruct[3])-1
    vers = int(instruct[5])-1
    for _ in range(combien):
        stacks1[vers].append(stacks1[depuis].pop())
        
result = ""
for stack in stacks1:
    result += stack[-1]
print("part1")
print(result)

# Part2

datas = open('5.txt')
line = datas.readline()
stacks2 = [[] for _ in range(9)]

while line !="\n":
    for i in range(9):
        index = 4 * i + 1
        carac = line[index]
        if carac.isalpha():
            stacks2[i] = [carac] + stacks2[i]
    line = datas.readline()
    
instructs = datas.readlines()


for line in instructs:
    instruct = line.split()
    combien = int(instruct[1])
    depuis = int(instruct[3])-1
    vers = int(instruct[5])-1
    stacks2[vers].extend(stacks2[depuis][-combien:])
    del stacks2[depuis][-combien:]
        
result = ""
for stack in stacks2:
    result += stack[-1]
print("part2")
print(result)
