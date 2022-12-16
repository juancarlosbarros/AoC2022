"""
AOC2022
Day13
"""


# Part 1
datas = open('13.txt')
d = []
for line in datas.readlines():
    if line != "\n":
        exec("d.append("+line.strip()+")")
# print(len(d)//2, "comparaisons...")

def ordered(l, r, final = True):
    # print("Compare:", l, r, sep = "#")
    if isinstance(l,int) and isinstance(r,int):
        if l > r:
            # print("End:", l, r, False, sep = "#")
            return False
        elif l < r:
            # print("End:", l, r, True, sep = "#")
            return True
        elif final: # si égalité et c'est le dernier nombre: True
            return True
        else: # sinon, retourne "continue"
            return "continue"
    elif isinstance(l,int) and isinstance(r,list):
        if r == []:
            # print("End:", l, r, False, sep = "#")
            return False
        else:
            # print("return:", [l], r)
            return ordered([l], r, final)
    elif isinstance(l,list) and isinstance(r,int):
        if l == []:
            # print("End:", l, r, True, sep = "#")
            return True
        else:
            # print("return:", l, [r])
            return ordered(l, [r], final)
    elif isinstance(l,list) and isinstance(r,list):
        if l == [] and r != []:
            # print("End:", l, r, True, sep = "#")
            return True
        elif l != [] and r == []:
            # print("End:", l, r, False, sep = "#")
            return False
        else:
            for el_l, el_r in zip(l, r):
                # print("return", el_l, el_r, sep = "#")
                res = ordered(el_l, el_r, False)
                if res == "continue":
                    continue
                else:
                    return res
            if len(l) > len(r):
                # print("End:", l, r, False, sep = "#")
                return False
            elif len(l) < len(r):
                # print("End:", l, r, True, sep = "#")
                return True
            elif final:  # si égalité et c'est le dernier nombre: True
                return True
            else:  # sinon, retourne "continue"
                return "continue"
    # print("End not reachable:", l, r, sep = "#")

def Part1():
    for el in d:
        # print(el)
        pass
    tot = 0
    for i in range(len(d)//2):
        res = ordered(d[2*i], d[2*i+1])
        if res:
            tot += i+1
            # print("Comp:", i+1, "Line:", 3*i+1)
            # print(d[2*i])
            # print(d[2*i+1])
            # print(res)

    print("Part1:")
    print(tot)

def tri_fusion(liste):
    if len(liste) <= 1:
        return liste
    milieu = len(liste)//2
    liste_gauche_triee = tri_fusion(liste[:milieu])
    liste_droite_triee = tri_fusion(liste[milieu:])
    reponse = fusion(liste_gauche_triee, liste_droite_triee)
    return reponse

def fusion(liste1_triee, liste2_triee):
    i = 0
    j = 0
    liste_triee = []
    while i < len(liste1_triee) and j < len(liste2_triee):
        if ordered(liste1_triee[i], liste2_triee[j]):
            liste_triee.append(liste1_triee[i])
            i += 1
        else:
            liste_triee.append(liste2_triee[j])
            j += 1
    if i < len(liste1_triee):
        liste_triee += liste1_triee[i:]
    else:
        liste_triee += liste2_triee[j:]
    return liste_triee


def tri_pivot(liste):
    if len(liste) <= 1:
        return liste
    liste_petits = []
    liste_grands = []
    # Définition du pivot:
    # 1er élément de la liste
    pivot = liste[0]
    # On parcourt tous les nombres
    # de la liste après le pivot
    for el in liste[1:]:
        if ordered(el, pivot):
            liste_petits.append(el)
        else:
            liste_grands.append(el)
    # On peut alors construire la réponse:
    # C'est la liste des petits triée,
    # le pivot, puis la liste des grands triée
    liste_triee = tri_pivot(liste_petits)
    liste_triee += [pivot]
    liste_triee += tri_pivot(liste_grands)
    return liste_triee


def Part2():
    d.extend([[[2]], [[6]]])
    d_sorted = tri_fusion(d)
    for line in d_sorted:
        # print(line)
        pass
    # print(d_sorted[d_sorted.index([[2]])], d_sorted[d_sorted.index([[6]])])
    print("Part2:")
    print((d_sorted.index([[2]])+1) * (d_sorted.index([[6]])+1))

Part1()
Part2()