from itertools import product

counter = 0
for i in product('AB123', repeat=8):
    a = ''.join(i)
    if (a.count('A') + a.count('B')) == 2:
        print(a)
        counter += 1
print(counter)
