import turtle

for x in range(4):
    turtle.forward(100)
    turtle.left(90)
turtle.up()
turtle.goto(50, 10)
turtle.down()
turtle.circle(40)

'''import random

a = random.randint(0, 10)

print(a)

size = input("Enter size of present small/midium/large: ")
style = input("Enter style for present classic/laplandia/modern: ")
if size == 'small' and style == 'classic':
    print("Red wrap with gold bow")
elif size == 'medium' or style == 'modern':
    print("Craft wrap with twine")
elif size == 'large':
    decoration = input("Add decoration?: ")
    if style == 'modern' and decoration == 'yes':
        print("White box with blue bow and bells")
    elif style == 'modern' and decoration == 'no':
        print("White box with blue bow and ribbon")
    if style == 'laplandia' and decoration == 'yes':
        print("Transparent wraping with snowflakes and bells")

    elif style == 'laplandia' and decoration == 'no':
        print("Transparent wraping with snowflakes and ribbon")

'''

