a = 'Jonny'
b = a + ' Braun'
print(id(a))
print(id(b))

print(a is b)
print(a, b)

c = [1, 2]
d = c
d.append('3')

print(id(c), id(d), c is d)
print(c, d)

f = c + [2]

print(id(c), id(d), id(f), c is f)

print(c, d, f)


for i in range(10):
    print('.' * i)
for i in range(8, 0, -1):
    print('.' * i)