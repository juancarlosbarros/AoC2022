"""
AOC2022
Day18
"""

datas = open('18.txt')
cubes = []
for line in datas.readlines():
    coord = line.strip().split(',')
    x = int(coord[0])
    y = int(coord[1])
    z = int(coord[2])
    cubes.append([x, y, z])

def Part1(cubes):
    tot_faces = 0
    for cube1 in cubes:
        faces = 6
        for cube2 in cubes:
            if abs(cube1[0] - cube2[0]) + abs(cube1[1] - cube2[1]) + abs(cube1[2] - cube2[2]) == 1:
                faces -= 1
        if faces < 0:
            print("oups, faces <0!")
        tot_faces += faces
    print(tot_faces)

Part1(cubes)
