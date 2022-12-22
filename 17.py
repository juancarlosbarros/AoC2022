"""
AOC2022
Day16
"""
from math import log


def Manhattan(pos1, pos2):
    delta_x = abs(pos1[0] - pos2[0])
    delta_y = abs(pos1[1] - pos2[1])
    return delta_x + delta_y


datas = open('16.txt')
sensors = []
beacons = []
for line in datas.readlines():
    parsed = line.strip().split()
    sensor_x = int(parsed[2][2:-1])
    sensor_y = int(parsed[3][2:-1])
    beacon_x = int(parsed[8][2:-1])
    beacon_y = int(parsed[9][2:])
    sensors.append((sensor_x, sensor_y))
    beacons.append((beacon_x, beacon_y))
# print(sensors)
# print(beacons)
nb_sensors = len(sensors)
y = 10 if len(sensors) == 14 else 2000000
max_xy = 20 if len(sensors) == 14 else 4000000
distances = [None for _ in range(len(sensors))]
for i in range(len(sensors)):
    dist = Manhattan(sensors[i], beacons[i])
    distances[i] = dist
# print(distances)

def count_cannot(y):
    can_list = []
    nb_cannot = 0
    cannot_list = []
    max_x = []
    min_x = []
    for i in range(len(sensors)):
        min_x.append(sensors[i][0] - distances[i] - abs(sensors[i][1] - y))
        max_x.append(sensors[i][0] + distances[i] - abs(sensors[i][1] - y))
    x_min = min(min_x)
    x_max = max(max_x)
    for x in range(x_min - 1, x_max + 1):
        cannot = False
        for i in range(len(beacons)):
            if Manhattan(sensors[i], (x, y)) <= distances[i] and (x, y) not in beacons:
                cannot = True
                break
        if cannot:
            nb_cannot += 1
            cannot_list.append(x)
    return nb_cannot

def Part1():
    print("Part1:")
    print(count_cannot(y))

# Part2
def can(candidate):
    """return True if (x, y) can be a hiden beacon"""

    for i in range(nb_sensors):
        can = True
        if Manhattan(sensors[i], candidate) <= distances[i]:
            can = False
            break
    return can


def find_line_hole(y):
    cannot = []
    candidates = []
    for i in range(len(sensors)):
        min_x = sensors[i][0] - (distances[i] - abs(sensors[i][1] - y))
        min_x = max(min_x, 0)
        max_x = sensors[i][0] + (distances[i] - abs(sensors[i][1] - y))
        max_x = min(max_x, max_xy)
        if min_x <= max_x:
            cannot.append((min_x, max_x))
    for i in cannot:
        for j in cannot:
            if j[0] == i[1] + 2:
                x = j[0] - 1
                for k in range(len(cannot)):
                    append_x = True
                    if (cannot[k][0] <= x <= cannot[k][1]) or (x, y) in beacons:
                        append_x = False
                        break
                if append_x == True and (x, y) not in candidates:
                    candidates.append((x,y))

    return candidates


def find_hole(max_xy):
    all_candidates = []
    for y in range(max_xy + 1):
        all_candidates = all_candidates + find_line_hole(y)
        if y % 100000 == 0:
            print("searching", y//100000, "%, nb_candidats:", len(all_candidates))
    return all_candidates


def Part2():
    print("Part2:")
    res = find_hole(max_xy)
    print(res[0][0] * 4000000 + res[0][1])

Part1()
Part2()