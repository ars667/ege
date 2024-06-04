c = '0123456789ABCDE'

for x in c:
    num1 = int('123' + x + '5', 15)
    num2 = int('1' + x + '233', 15)
    if (num1 + num2) % 14 == 0:
        print((num1 + num2) // 14)
