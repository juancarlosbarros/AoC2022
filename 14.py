"""
AOC2022
Day14
"""

datas = open('14.txt')
d = []
for line in datas.readlines():
    d.append([(int(point.split(",")[0]), int(point.split(",")[1])) for point in line.strip().split(" -> ")])
x_values = []
y_values = []
for path in d:
    for point in path:
        x_values.append(point[0])
        y_values.append(point[1])
x_min = min(x_values)
x_max = max(x_values)
y_min = min(y_values)
y_max = max(y_values)

def x_(x):
    return x-x_min

def y_(y):
    return y

def xy_(x, y):
    return x_(x), y_(y)

grid = [['.' for x in range(x_(x_max)+1)] for y in range(y_(y_max)+1)]
grid[y_(0)][x_(500)] = '+'
for path in d:
    first_point = True
    for point in path:
        actual_x, actual_y = point
        if first_point:
            prec_point_x = actual_x
            prec_point_y = actual_y
            first_point = False
        elif actual_x == prec_point_x:
            if actual_y < prec_point_y:
                pas = -1
            else:
                pas = 1
            for y in range (prec_point_y, actual_y+pas, pas):
                grid[y_(y)][x_(actual_x)] = '#'
        elif actual_y == prec_point_y:
            if actual_x < prec_point_x:
                pas = -1
            else:
                pas = 1
            for x in range (prec_point_x, actual_x+pas, pas):
                grid[y_(actual_y)][x_(x)] = '#'
        prec_point_x = actual_x
        prec_point_y = actual_y

grid2 = grid[:] # pour Part2

def affiche(grid):
    for line in grid:
        print("".join(line))

def chute(grid):
    x = 500
    y = 0
    fall = True
    while fall and y<y_max:
        fall = False
        if grid[y_(y+1)][x_(x)] == '.':
            y += 1
            fall = True
        elif grid[y_(y+1)][x_(x-1)] == '.':
            y += 1
            x -= 1
            fall = True
        elif grid[y_(y+1)][x_(x+1)] == '.':
            y += 1
            x += 1
            fall = True
    if 0 < y < y_max:
        grid[y_(y)][x_(x)] = 'o'
        return grid, True
    else:
        return grid, False

# Part 1
def Part1():
    global grid
    falls = 0
    not_full = True
    while not_full:
        falls += 1
        grid, not_full = chute(grid)
    # affiche(grid)
    print("Part1:")
    print(falls-1)
Part1()


# Part2
THICK = 1000
grid2 = [['.'] * THICK + line + ['.'] * THICK for line in grid2]
grid2.append(['.'] * (2*THICK + x_max - x_min + 1))
grid2.append(['#'] * (2*THICK + x_max - x_min + 1))
y_max += 2
x_min -= THICK
x_max += THICK
# affiche(grid2)
falls = 0
not_full = True
while not_full:
    falls += 1
    grid2, not_full = chute(grid2)
# affiche(grid2)
print("Part2:")
print(falls)