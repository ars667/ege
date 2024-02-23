print('w y z x')
def f(w, y, z, x):
    return (x or not(y)) and not(y == z) and w
for w in range(2):
    for x in range(2):
        for y in range(2):
            for z in range(2):
                if f(w, y, z, x) == 1:
                    print(w, y, z, x)


