# ...записали в системе с осн 8, сколько "7"

a = 64 ** 30 + 2 ** 300 - 4

# алгоритм перевода в другую систему
num = ''
while a > 0:
    num += str(a % 8)
    a = a // 8

# не забываем реверс строки
num = num[::-1]

print(num.count('7'))
