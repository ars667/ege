f = open('9_2091.csv')
topic = f.readline().split(';')
arr = []
line = f.readline()
while line:
    arr.append([line.split(';')[0], int(line.split(';')[1]), int(line.split(';')[2]), int(line.split(';')[3])])
    line = f.readline()
print(arr)

counter = 0
for i in range(len(arr)):
    if arr[i][1] == 1 and (arr[i][2] >= 85 or arr[i][3] >= 85):
        counter += 1
        print(arr[i])
print(counter)
