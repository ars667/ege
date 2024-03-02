d = '0123456789AB'

a = 6*144**26 + 11*12**75 - 48

num = ''
while a > 0:
    num += d[a % 12]
    a = a // 12
print(num.count('B'))
