print('Let\'s parse CSV file.\n')
file = open('random_data.csv', 'r')
data = []
string = file.readline()
while string:
    lst = string.split(',')
    for el in lst:
        print(el)
    string = file.readline()
file.close()