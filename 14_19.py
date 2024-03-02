def f(n, system):
    a = n
    num = ''
    while a > 0:
        num += str(a % system)
        a = a // system
    num = num[::-1]
    return num


counter = 0

for i in range(0, 100000):
    n_5 = f(i, 5)
    n_2 = f(i, 2)
    if len(n_5) <= 4 and len(n_2) >= 5 and hex(i)[-1] == 'c':
        counter += 1
print(counter)
