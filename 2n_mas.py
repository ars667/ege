m = 500
a = [[[0] * m for _ in range(m)] for _ in range(m)]
b = [[False] * m for _ in range(m)]

for i in range(m - 1, 0, -1):
    for j in range(m - 1, 0, -1):
        if i * j >= 63:
            a[i][j][k] = 0
            continue

        moves = [a[i + 1][j], a[i][j + 1], a[i * 2][j], a[i][j * 2]]
        b[i][j] = 1 in moves
        if min(moves) <= 0:
            a[i][j] = 1 - max([x for x in moves if x <= 0])
            continue
        a[i][j] = -1 - max(moves)
for x in range(1, 32):
    if a[x][2] == -2:
        print(x)
