from itertools import permutations

gl = 'аиоу'
sg = 'бклн'
k = 0

for i in permutations('абиколун', r=8):
    a = ''.join(i)
    if all((a[i] in gl and a[i+1] in sg) or (a[i] in sg and a[i+1] in gl) for i in range(7)):
        k += 1
print(k)
