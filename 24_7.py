f = open('24_2251.txt').readline()

m = c = l = r = 0
for i in range(len(f)):
    if f[i] == 'D':
        c += 1
    r += 1
    while c > 2:
        l += 1
        if f[l] == 'D':
            c -= 1
    m = max(m, r - l - 1)
print(m)
