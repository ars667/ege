from itertools import permutations

counter = 0
for i in permutations('ИГРОК', r=5):
    word = ''.join(i)
    if word[0] != 'К' and not ('РОК' in word):
        print(word)
        counter += 1
print(counter)
