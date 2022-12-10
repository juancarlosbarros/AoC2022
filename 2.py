"""
AOC2022
Day2
"""
# Part 1
f = open('2.txt')
scores = []
for game in f:
    # print(game)
    player1 = ord(game[0])-ord('A')
    player2 = ord(game[2])-ord('X')
    score = player2 + 1
    diff = (player2-player1) % 3
    if diff == 0:
        score += 3
    elif diff == 1:
        score += 6
    scores.append(score)
print("Part 1")
print(sum(scores))

# Part 2
f = open('2.txt')
scores = []
for game in f:
    # print(game)
    player1 = ord(game[0])-ord('A')
    result = ord(game[2])-ord('X')
    if result == 0:
        player2 = (player1-1) % 3
        score = player2 + 1
    elif result == 1:
        player2 = player1
        score = player2 + 4
    else:
        player2 = (player1+1) % 3
        score = player2 + 7
    scores.append(score)
print("Part 2")
print(sum(scores))
