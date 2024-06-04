# строка, записанная в файле, оказалась в переменной
f = open('24_1040.txt').readline()
for i in range(ord('a'), ord('z')+1):
    f = f.replace(chr(i), ' ')
print(f)
print(max([len(x) for x in f.split()]))
