for i in range(174457, 174505 + 1):
    num = 0
    mas = []
    for j in range(2, i):
        if i % j == 0:
            mas.append(j)
            num += 1
    if num == 2:
        print(mas)
