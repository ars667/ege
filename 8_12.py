from itertools import product

k = 0
for i in product('ABCD', repeat=4):
    a = ''.join(i)

    # создаём копию, заменяя буквы цифрами
    b = a
    b = b.replace('A', '1')
    b = b.replace('B', '2')
    b = b.replace('C', '3')
    b = b.replace('D', '4')

    # разбиваем строку b на символы и загоняем в массив
    mas = [x for x in b]

    # если при сортировке ничего ничего не изменилось, был алфавитный порядок
    if mas == sorted(mas):
        print(a)
        k += 1
print(k)
