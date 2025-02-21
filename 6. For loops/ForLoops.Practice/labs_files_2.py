text_file = open('data.txt', encoding='utf8')
line = text_file.readline()
lst = []
while line:
    line = line.split()
    s = line[0]
    s = s[:-1]
    lst.append((s, int(line[1])))
    line = text_file.readline()
text_file.close()

for x, y in lst:
    if y < 10:
        print(x)