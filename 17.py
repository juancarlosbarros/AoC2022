from itertools import cycle

"""
AOC2022
Day17
"""

datas = open('17.txt')
directions = datas.readline()
jets = []
for jet in directions:
    if jet == '<':
        jets.append(-1)
    elif jet == '>':
        jets.append(1)
    else:
        print("Erreur de lecture:", jet)
jets_cycle = cycle(jets)
shapes = [[[0, 0], [1, 0], [2, 0], [3, 0]], [[1, 0], [0,1], [1, 1], [2, 1], [1, 2]],
         [[0, 0], [1, 0], [2, 0], [2, 1], [2, 2]], [[0, 0], [0, 1], [0, 2], [0, 3]],
          [[0, 0], [0, 1], [1, 0], [1, 1]]]
shapes_cycle = cycle(shapes)

def move_jet(shape, jet, rocks, min_x, max_x):
    new_shape = []
    for i in range(len(shape)):
        new_x = shape[i][0] + jet
        y = shape[i][1]
        if min_x <= new_x <= max_x and [new_x, y] not in rocks:
            new_shape.append([new_x, y])
        else:
            return shape
    return new_shape


def land(shape, rocks):
    for pixel in shape:
        if [pixel[0], pixel[1] - 1] in rocks:
            return True # landed!
    return False


def move_fall(shape):
    for i in range(len(shape)):
        shape[i][1] -= 1
    return shape


def h(shape):
    h = 0
    for pixel in shape:
        if pixel[1] > h:
            h = pixel[1]
    return h


def affiche(rocks, shape, height):
    y = 0
    grid = []
    while y <= height+6:
        line = ""
        for x in range(1,8):
            if [x, y] in rocks:
                line += '#'
            elif [x, y] in shape:
                line += '@'
            else:
                line += '.'
        grid.append(line)
        y += 1
    print()
    for line in reversed(grid):
        print(line)



def Part1(nb_rocks):
    rocks = [[x, 0] for x in range(1, 8)]  # fond = ligne de roche
    height = 0
    start_delta_y = 4
    start_delta_x = 3
    min_x = 1
    max_x = 7
    nb_shapes = 0
    while nb_shapes < nb_rocks:
        if nb_shapes % 1000 == 0:
            print(nb_shapes)
        shape_list = next(shapes_cycle)
        shape = [[pixel[0] + start_delta_x, pixel[1] + start_delta_y + height] for pixel in shape_list]
        landed = False
        while not landed:
            # affiche(rocks, shape, height+1)
            jet = next(jets_cycle)
            shape = move_jet(shape, jet, rocks, min_x, max_x)
            landed = land(shape, rocks)
            if landed:
                rocks.extend(shape)
                h_shape = h(shape)
                if h_shape > height:
                    height = h_shape
                # affiche(rocks, shape, height + 1)
            else:
                shape = move_fall(shape)
        nb_shapes += 1
    return height


# print(Part1(2022))
print(Part1(1000000000000))