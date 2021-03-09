# Andrew Riker
# CS1400 - LW2 XL
# Assignment #03

# enter investment amount
investmentAmt = eval(input("Enter the starting investment amount: $"))
# enter monthly payment amount
monthlyPay = eval(input("Enter monthly payment amount: $"))
# enter annual interest rate
annualInterestRate = eval(input("Enter the annual interest rate: eg, 4.5 "))
# enter number of years
numYears = eval(input("Enter the number of years: "))

# calculate number of months and monthly interest rate
monthlyInterestRate = annualInterestRate / 1200
months = numYears * 12

# calculate final value
finalValue = investmentAmt * ((1 + monthlyInterestRate) ** months) + monthlyPay * \
             ((1 + monthlyInterestRate) ** months - 1) / monthlyInterestRate * (1 + monthlyInterestRate)

# print the final value
print("Final Value is $" + str(round(finalValue, 2)))
