m = 300
a = [0] * m
b = [False] * m

for i in range(0, m):
    if i == 0:
        a[i] = 0
        continue
    moves = []
    if i - 1 >= 0:
        moves = [a[i - 1]]
    if i - 2 >= 0:
        moves.append(a[i - 2])
    if i - 4 >= 0:
        moves.append(a[i - 4])

    b[i] = 1 in moves
    if min(moves) <= 0:
        # можем выигрыть
        # максимум из массива тех элкементов из moves, которые <= 0
        a[i] = 1 - max([x for x in moves if x <= 0])
    else:
        # можем только проиграть, поэтому пытаемся как можно дольше
        a[i] = -1 - max(moves)
for i in range(15):
    print(i, a[i], b[i])
