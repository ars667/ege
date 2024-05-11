m = 300
a = [[0] * m for _ in range(m)]

for i in range(m - 1, -1, -1):
    for j in range(m - 1, -1, -1):
        if i + j >= 59:
            a[i][j] = 0
            continue
        moves = [a[i + 1][j], a[i][j + 1],a[i * 2][j], a[i][j * 2]]

        if min(moves) <= 0:
            a[i][j] = 1 - max([x for x in moves if x <= 0])
        else:
            a[i][j] = -1 -max(moves)
for s in range(1, 53):
    print(s, a[5][s])
