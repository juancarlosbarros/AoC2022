from copy import deepcopy

"""
AOC2022
Day11
"""


# Part 1
datas = open('11.txt')
Nb_monks = 8
monk_items = [[] for _ in range(Nb_monks)]
monk_process = [{} for _ in range(Nb_monks)]

for i in range(Nb_monks):
    datas.readline()
    line = datas.readline()
    parsed_line = line.strip().split(":")[1].strip().split(", ")
    start_items = [int(item) for item in parsed_line]
    # print(start_items)
    monk_items[i].extend(start_items)
    for cat in ['op', 'test', 'true', 'false']:
        parsed_line = datas.readline().strip().split()
        # parsed_line = deepcopy(parsed_line)
        if cat == 'op': # doesn't work!
            if parsed_line[-2] == "+":
                nb = int(parsed_line[-1])
                monk_process[i]['op'] = lambda x: x + nb
            elif parsed_line[-2] == "*":
                if parsed_line[-1] == 'old':
                    monk_process[i]['op'] = lambda x: x ** 2
                else:
                    nb = int(parsed_line[-1])
                    monk_process[i]['op'] = lambda x: x * nb
        else:
            monk_process[i][cat] = int(parsed_line[-1])
    datas.readline()
if Nb_monks == 8:
    monk_process[0]['op'] = lambda x: x * 2
    monk_process[1]['op'] = lambda x: x + 3
    monk_process[2]['op'] = lambda x: x + 6
    monk_process[3]['op'] = lambda x: x + 5
    monk_process[4]['op'] = lambda x: x + 8
    monk_process[5]['op'] = lambda x: x * 5
    monk_process[6]['op'] = lambda x: x ** 2
    monk_process[7]['op'] = lambda x: x + 4
elif Nb_monks == 4:
    monk_process[0]['op'] = lambda x: x * 19
    monk_process[1]['op'] = lambda x: x + 6
    monk_process[2]['op'] = lambda x: x ** 2
    monk_process[3]['op'] = lambda x: x + 3

monk_business = [0 for _ in range(Nb_monks)]
def monk_round():
    for i in range(len(monk_items)):
        for item in monk_items[i]:
            monk_business[i] += 1
            result = monk_process[i]['op'](item)
            result = result // 3
            if result % monk_process[i]['test'] == 0:
                monk_items[monk_process[i]['true']].append(result)
            else:
                monk_items[monk_process[i]['false']].append(result)
        monk_items[i] = []
def monk_show():
    print("Items by monkey:")
    for i in range(len(monk_items)):
        print("Monkey", i, ": ", monk_items[i])

# monk_show()
for i in range (1, 21):
    monk_round()
    # print("After round ", i)
    # monk_show()
print("Part1:")
print(sorted(monk_business)[-2] * sorted(monk_business)[-1])


# Part 2
datas = open('11.txt')
monk_items = [[] for _ in range(Nb_monks)]
monk_process = [{} for _ in range(Nb_monks)]

for i in range(Nb_monks):
    datas.readline()
    line = datas.readline()
    parsed_line = line.strip().split(":")[1].strip().split(", ")
    start_items = [int(item) for item in parsed_line]
    # print(start_items)
    monk_items[i].extend(start_items)
    for cat in ['op', 'test', 'true', 'false']:
        parsed_line = datas.readline().strip().split()
        # parsed_line = deepcopy(parsed_line)
        if cat == 'op': # doesn't work!
            if parsed_line[-2] == "+":
                nb = int(parsed_line[-1])
                monk_process[i]['op'] = lambda x: x + nb
            elif parsed_line[-2] == "*":
                if parsed_line[-1] == 'old':
                    monk_process[i]['op'] = lambda x: x ** 2
                else:
                    nb = int(parsed_line[-1])
                    monk_process[i]['op'] = lambda x: x * nb
        else:
            monk_process[i][cat] = int(parsed_line[-1])
    datas.readline()

diviseur_global = 1
for monk in monk_process: 
    diviseur_global *= monk['test']

# saisie manuelle bidon, faute de mieux...
if Nb_monks == 8:
    monk_process[0]['op'] = lambda x: (x * 2) % diviseur_global
    monk_process[1]['op'] = lambda x: (x + 3) % diviseur_global
    monk_process[2]['op'] = lambda x: (x + 6) % diviseur_global
    monk_process[3]['op'] = lambda x: (x + 5) % diviseur_global
    monk_process[4]['op'] = lambda x: (x + 8) % diviseur_global
    monk_process[5]['op'] = lambda x: (x * 5) % diviseur_global
    monk_process[6]['op'] = lambda x: (x ** 2) % diviseur_global
    monk_process[7]['op'] = lambda x: (x + 4) % diviseur_global
elif Nb_monks == 4:
    monk_process[0]['op'] = lambda x: (x * 19) % diviseur_global
    monk_process[1]['op'] = lambda x: (x + 6) % diviseur_global
    monk_process[2]['op'] = lambda x: (x ** 2) % diviseur_global
    monk_process[3]['op'] = lambda x: (x + 3) % diviseur_global
    
# print(monk_process)
        
monk_business = [0 for _ in range(Nb_monks)]
def monk_round_2():
    for i in range(len(monk_items)):
        for item in monk_items[i]:
            monk_business[i] += 1
            result = monk_process[i]['op'](item)
            # result = result // 3
            if result % monk_process[i]['test'] == 0:
                monk_items[monk_process[i]['true']].append(result)
            else:
                monk_items[monk_process[i]['false']].append(result)
        monk_items[i] = []

# monk_show()
for i in range (1, 10001):
    monk_round_2()
    # print("After round ", i)
# monk_show()
print("Part2:")
print(sorted(monk_business)[-2] * sorted(monk_business)[-1])