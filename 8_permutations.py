# меняют местами буквы в МИМИКРИЯ, сколько получится слов?

# перестановки - permutations

from itertools import permutations

difs = set()

word = 'мимикрия'
for i in permutations(word, r=8):
    current = ''.join(i)
    difs.add(current)
print(len(difs))
