f = open('24_2422.txt').readline()

c = 1
m = 0

for i in range(len(f)-1):
    if ord(f[i]) <= ord(f[i+1]):
        c += 1
    else:
        m = max(m, c)
        c = 1
print(m)
