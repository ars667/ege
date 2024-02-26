from itertools import permutations

ъ = '01234567'
чётные = '0246'
нечётные = '1357'
counter = 0

for i in permutations(ъ, r=5):
    a = ''.join(i)
    if not (a[0] == '0') and not ('1' in a) and all(
            (a[i] in чётные and a[i + 1] in нечётные) or (a[i] in нечётные and a[i + 1] in чётные) for i in range(4)):
        print(a)
        counter += 1
print(counter)
