a = 51 * 7 ** 12 - 7 ** 3 - 22

num = ''
while a > 0:
    num += str(a % 7)
    a = a // 7

num = num[::-1]

s = 0
for digit in num:
    s = s + int(digit)
print(s)
