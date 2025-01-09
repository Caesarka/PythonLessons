print("Let's calculate your morgage payment")
principalLoanAmount = float(input("Enter the principal loan amount: "))
interestRate = float(input("Enter the interest rate on your loan: ")) /100 / 12
repaymentLength = float(input('How many years will you have the loan: ')) * 12
mortgagePayment = round(principalLoanAmount * (interestRate * (1 + interestRate) ** repaymentLength) / ((1 + interestRate) ** repaymentLength - 1))
print(f"The monthly mortgage payment is ${mortgagePayment}")