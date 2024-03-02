d = '0123456789A'

for n in range(1, 1000):
    a = n

    num_6 = ''
    while n > 0:
        num_6 += str(n % 6)
        n = n // 6
    num_6 = num_6[::-1]

    n = a

    num_5 = ''
    while n > 0:
        num_5 += str(n % 5)
        n = n // 5
    num_5 = num_5[::-1]

    n = a

    num_11 = ''
    while n > 0:
        num_11 += d[n % 11]
        n = n // 11
    num_11 = num_11[::-1]

    if len(num_6) == 2 and len(num_5) == 3 and num_11[-1] == '1':
        print(a)
