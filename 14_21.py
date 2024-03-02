g = '0123456789ABCDEFG'

for x in g:
    x1 = int('9759' + x, 17)
    x2 = int('3' + x + '108', 17)
    if (x1 + x2) % 11 == 0:
        print((x1 + x2) // 11)
