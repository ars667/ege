for n in range(2, 30):
    a = 68
    v = ''
    while a > 0:
        v += str(a % n)
        a = a // n
    v = v[::-1]
    if v[-1] == '2' and len(v) == 4:
        print(n)
