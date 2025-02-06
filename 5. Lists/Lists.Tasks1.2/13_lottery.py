
import random
print("Let's check your lottery ticket!")
lucky_numbers = random.sample(range(1, 49), 6)
lucky_numbers.sort()

lollery_ticket = (input("Enter your numbers, use space as delimiter: "))

lst = list(map(int, lollery_ticket.split()))
lst.sort()

print(f"Lottery numbers: {' '.join(map(str, lucky_numbers))}")
print(f"Your numbers: {' '.join(map(str, lst))}")
if lucky_numbers == lst:
    print("Hooray! You won the lottery!")
else:
    print("Unfortunately, you didn't win this time.")