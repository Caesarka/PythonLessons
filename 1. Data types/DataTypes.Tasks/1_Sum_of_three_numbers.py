while True:
     try:
          firstNum = float(input("Enter first number: "))
          secondNum = float(input("Enter second number: "))
          thirdNum = float(input("Enter third number: "))
          sum = round(firstNum + secondNum + thirdNum, 2)
          print(f"Sum of three numbers equals {sum}")
     except:
          print("Please enter a numbers")
     print()

     usrInput = input("Press any key to continue or q to exit ")

     if usrInput == 'q':
          break

