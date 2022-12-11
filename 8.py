"""
AOC2022
Day8
"""

# Part 1
datas = open('8.txt')
heights = datas.readlines()
h = [] # matrix of heights
for line in heights:
    line = line.strip()
    line_int = [int(height) for height in line]
    h.append(line_int)

def visible(y, x):
    h_self = h[y][x]
    # visible à gauche?
    vis_L = True
    for i in range(0, x):
        if h[y][i] >= h_self:
            vis_L = False
    if vis_L:
        return True
    # visible à droite?
    vis_R = True
    for i in range(x+1, len(h[0])):
        if h[y][i] >= h_self:
            vis_R = False
    if vis_R:
        return True
    # visible en-haut?
    vis_U = True
    for i in range(0, y):
        if h[i][x] >= h_self:
            vis_U = False
    if vis_U:
        return True
    # visible en-bas?
    vis_D = True
    for i in range(y+1, len(h)):
        if h[i][x] >= h_self:
            vis_D = False
    if vis_D:
        return True
    # No ? So it's not visible!
    return False
    

tot_visibles = 0
for i in range(len(h)):
    for j in range(len(h[0])):
        if visible(i, j):
            tot_visibles += 1

print("Part1")
print(tot_visibles)

# Part2

def score(y, x):
    h_self = h[y][x]
    # arbres visibles à gauche?
    vis_L = 0
    for i in range(1, x+1):
        vis_L += 1
        if h[y][x-i] >= h_self:
            break            
    # arbres visibles à droite?
    vis_R = 0
    for i in range(x+1, len(h[0])):
        vis_R += 1
        if h[y][i] >= h_self:
            break            
    # arbres visibles en-haut?
    vis_U = 0
    for i in range(1, y+1):
        vis_U += 1
        if h[y-i][x] >= h_self:
            break            
    # arbres visibles à droite?
    vis_D = 0
    for i in range(y+1, len(h)):
        vis_D += 1
        if h[i][x] >= h_self:
            break            
    return vis_L*vis_R*vis_U*vis_D

# print(score(3, 2))
max_score = 0
for i in range(len(h)):
    for j in range(len(h[0])):
        score_test = score(i, j)
        if score_test > max_score:
            max_score = score_test

print("Part2")
print(max_score)
