arr = []
for n in range(1, 10000):
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        bin_n += '01'
    else:
        bin_n += '10'
    arr.append(int(bin_n, 2))
print(arr)