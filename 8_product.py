# сколько слов, начинающихся с согласной, заканчивающихся гласной, можно составить из КРЕСЛО. Могут повторяться

# product - могут повторяться
from itertools import product

counter = 0
word = 'кресло'
sogl = 'крсл'
gl = 'ео'
for i in product(word, repeat=4):
    current = ''.join(i)
    if current[0] in sogl and current[-1] in gl:
        counter += 1
print(counter)
