from tabulate import tabulate

print("Table conversion from degrees Celsius to degrees Fahrenheit")
celsius = 10
headers = ['Celsius', 'Fahrenheit']
conversion = []
while celsius <= 100:
    conversion.append((celsius, ((celsius * 9 / 5) + 32)))
    celsius += 10

#print(conversion)
print(tabulate(conversion, headers=headers, tablefmt="fancy_grid"))


