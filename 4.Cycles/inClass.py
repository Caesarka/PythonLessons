'''
k = 10
digits_to_words = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10:"ten"
    }
while k >= 0:
    print(digits_to_words[k])
    k -= 1
print("Poleteli!")
'''

'''

from random import randint

from tkinter import *
 
root = Tk()     # создаем корневой объект - окно
root.title("Приложение на Tkinter")     # устанавливаем заголовок окна
root.geometry("300x250")    # устанавливаем размеры окна
 
label = Label(text="Hello METANIT.COM") # создаем текстовую метку
label.pack()    # размещаем метку в окне
 
root.mainloop()
 


while True:
    rndNumber = randint(0, 100)
    numberOfGuess = 3
    while numberOfGuess > 0:
        number = input(f"Try to guess number from 0 to 100. Guess {numberOfGuess}: ")
        if number == rndNumber:
            print("Yes! You're right!!")
            break
        else:
            print("Nope...")
            numberOfGuess -= 1
            
    usrInput = input("Let's try again? Y/N: ")
    if usrInput != "Y":
        break
'''
import random
index = int(input("Enter index: "))
a = 1
b = 1
i = 1
while i <= index:
    sum = a + b
    a = b
    b = sum
    i += 1
    if i == index: break


print(b)