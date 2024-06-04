def f(x, y, w, z):
    return (x or not (y)) and not (y == z) and w


print('x y w z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x, y, w, z) == 1:
                    print(x, y, w, z)
