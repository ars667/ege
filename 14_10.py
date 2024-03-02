a = 5 * 216 ** 1156 - 4*36**1147 + 6**1153 - 875

k = ''
while a > 0:
    k += str(a % 6)
    a = a // 6
print(k.count('5') - k.count('0'))
