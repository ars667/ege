# в условии было сказано: траектория вычислений содержит 10

def f(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    if a < b:
        return f(a + 1, b) + f(a * 2, b)


print(f(1, 10) * f(10, 20))
