def f(x, y, a):
    return not ((x * y > a) and (x > y) and (x < 8))


for a in range(100000):
    if all(f(x, y, a) for x in range(1000) for y in range(1000)):
        print(a)
