"""
AOC2022
Day12
"""


# Part 1
datas = open('12.txt')
datas = datas.readlines()
grid = [[ord(cell)-ord('a') for cell in line.strip()] for line in datas]
# gestion de S et E
trouve = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == ord('S') - ord('a'):
            S = (j, i)
            grid[i][j] = 0
            trouve += 1
        elif grid[i][j] == ord('E') - ord('a'):
            E = (j, i)
            grid[i][j] = 25
            trouve += 1
        if trouve == 2:
            break

neighbours = {(x, y):{} for x in range(len(grid[0])) for y in range(len(grid))}
max_x = len(grid[0])
max_y = len(grid)
for i in range(max_y):
    for j in range(max_x):
        # recherche voisins atteignables horizontalement
        for delta_x in [-1, 1]:
            if 0 <= j+delta_x <= max_x-1:
                delta_h = grid[i][j+delta_x] - grid[i][j]
                if delta_h <= 1:
                    neighbours[(j, i)][j+delta_x,i] = delta_h
        # recherche voisins atteignables verticalement
        for delta_y in [-1, 1]:
            if 0 <= i+delta_y <= max_y-1:
                delta_h = grid[i+delta_y][j] - grid[i][j]
                if delta_h <= 1:
                    neighbours[(j, i)][j,i+delta_y] = delta_h


def mannathan(A, B):
    """
    distance mannathan entre points A et B
    """
    return abs(A[0] - B[0]) + abs(A[1] - B[1])
    
def Astar(S, E, grid, neighbours):
    queue = {S:0} # order: (dist + mannathan) 
    predecessors = {S:None}
    distances = {S:0}
    while len(queue) > 0:
        min_heur = min(queue.values())
        actual = [key for key, value in queue.items() if value == min_heur][0]
        for neighbour in neighbours[actual]:
            dist = distances[actual] + 1
            if not (neighbour in predecessors and distances[neighbour] <= dist):
                distances[neighbour] = dist
                predecessors[neighbour] = actual
                queue[neighbour] = dist + mannathan(neighbour, E)
            if neighbour == E:
                break
        queue.pop(actual)
    return distances, predecessors

def Part1():
    distances, predecessors = Astar(S, E, grid, neighbours)
    path = [E]
    retro_path = E
    while retro_path != S:
        retro_path = predecessors[retro_path]
        path = [retro_path] + path
    print("Part1")
    print(distances[E])

Part1()

# Part2
# Liste de toutes les cases 'a', donc 0 (dans grid)
def Part2():
    a = []
    for i in range(max_y):
        for j in range(max_x):
            if grid[i][j] == 0:
                a.append((j,i))
    # 990 'a' !!!

    min_dist = 1000
    for start in a:
        distances, predecessors = Astar(start, E, grid, neighbours)
        if E in distances:
            dist = distances[E]
            if dist < min_dist:
                # print(start, dist)
                min_dist = dist
    print("Part2")
    print(min_dist)

Part2()

    