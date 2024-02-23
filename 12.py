line = ('8' * 70)
while '2222' in line or '8888' in line:
    if '2222' in line:
        line = line.replace('2222', '88', 1)
    else:
        line = line.replace('8888', '22', 1)
print(line)