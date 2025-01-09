print("Let's convert temperature from Fahrenheits to Celsius")
tempInFahrenheits = float(input("Enter temperature in Fahrenheits: "))
tempInCelsius = round((tempInFahrenheits - 32) / 1.8, 2)
print(f"{tempInFahrenheits}° Fahrenheits equal {tempInCelsius}° Celsius")