"""
AOC2022
Day9
"""

U = (0, 1)
D = (0, -1)
L = (-1, 0)
R = (1, 0)
def mouv(H, T):
    delta = (H[0]-T[0],H[1]-T[1])
    if delta[0]**2 + delta[1]**2 <= 2:
        return T
    elif delta[0] == 0 or delta[1] == 0:
        return (T[0]+delta[0]//2,T[1]+delta[1]//2)
    elif delta[1]**2 == 1:
        return (T[0]+delta[0]//2,T[1]+delta[1])
    elif delta[0]**2 == 1:
        return (T[0]+delta[0],T[1]+delta[1]//2)
    elif delta[0]**2 == 4 and delta[1]**2 == 4:
        return (T[0]+delta[0]//2,T[1]+delta[1]//2)
    else:
        print(H, T, delta)


# Part 1
datas = open('9.txt')
H_pos = (0, 0) # (x, y)
T_pos = (0, 0)
visited = {T_pos}
instructions = datas.readlines()

for instr in instructions:
    instr = instr.strip().split()
    vec = globals()[instr[0]]
    for _ in range(int(instr[1])):
        H_pos = (H_pos[0]+vec[0],H_pos[1]+vec[1])
        T_pos = mouv(H_pos, T_pos)
        visited.add(T_pos)
        
print("Part1")
print(len(visited))

# Part2
pos = [(0, 0) for _ in range(10)] # (x, y)
visited = {(0,0)}
for instr in instructions:
    instr = instr.strip().split()
    vec = globals()[instr[0]]
    for _ in range(int(instr[1])):
        pos[0] = (pos[0][0]+vec[0],pos[0][1]+vec[1])
        for i in range(1,10):
            pos[i] = mouv(pos[i-1], pos[i])
        visited.add(pos[9])
        
print("Part2")
print(len(visited))