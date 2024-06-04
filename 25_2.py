for i in range(81234, 134689+1):
    if abs(i**0.5 - round(i**0.5)) > 0.000000001:
        continue
    mas = []
    for j in range(2, round(i**0.5)):
        if i % j == 0:
            mas.append(j)
            mas.append(i // j)
    if len(mas) == 2:
        print(mas)
