d = '0123456789ABCDEFGH'
for x in d:
    if all((int('12' + y + x + '9', 21) + int('36' + y + '99', 21)) % 18 == 0 for y in d):
        y = '5'
        print((int('12' + y + x + '9', 21) + int('36' + y + '99', 21)) // 18)
