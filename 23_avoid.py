def f(a, b):
    if a == 12 or a == 6:
        return 0
    if a > b:
        return 0
    if a == b:
        return 1
    if a < b:
        return f(a + 1, b) + f(a * 2, b) + f(a + 3, b)


print(f(3, 16))
