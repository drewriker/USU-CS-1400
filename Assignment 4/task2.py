# Andrew Riker
# CS1400 - LW2 XL
# Assignment #04

# user enters name of employee
name = input("Enter employee's name: ")
# user enters number of hours worked in a week
numberOfHours = eval(input("Enter number of hours worked in a week: "))
# user enters hourly pay
payRate = eval(input("Enter hourly pay rate: "))
# user enters federal tax rate
federalTaxRate = eval(input("Enter federal tax withholding rate (ex. 0.12): "))
# user enters state tax rate
stateTaxRate = eval(input("Enter state tax withholding rate (ex. 0.06): "))


# get federal percentage
federalPercent = str(format(federalTaxRate, "2.1%"))
# get state percentage
statePercent = str(format(stateTaxRate, "1.1%"))


# calculate gross pay
grossPay = numberOfHours * payRate
# calculate federal withholding
federalWithhold = grossPay * federalTaxRate
# calculate state withholding
stateWithhold = grossPay * stateTaxRate
# total deductions
totalDeductions = stateWithhold + federalWithhold
# net pay
netPay = grossPay - totalDeductions

# spec for format
specString = ">30s"
specFloat = "10.2f"


# name + pay information
msg = "\n\t" + name.upper() + " pay information".upper()
# pay
msg += "\n" + str(format("Pay", ">25s"))
msg += "\n"

# hours worked
msg += format("Hours Worked:  ", specString) + str(format(numberOfHours, "10.0f"))
msg += "\n"
# Pay rate
msg += format("Pay Rate: $", specString) + str(format(payRate, specFloat))
msg += "\n"
# gross pay
msg += format("Gross Pay: $", specString) + str(format(grossPay, specFloat))
msg += "\n"

# print Deductions
msg += "\n" + str(format("Deductions", ">25s"))
msg += "\n"
# Federal Withholding
msg += format("Federal Withholding (" + federalPercent + "): $", specString) + str(format(federalWithhold, specFloat))
msg += "\n"
# state withholding
msg += format("State Withholding (" + statePercent + "): $", specString) + str(format(stateWithhold, specFloat))
msg += "\n"
# Total deductions
msg += format("Total Deduction: $", specString) + str(format(totalDeductions, specFloat))
msg += "\n"
# net pay
msg += "\n"
msg += format("Net Pay: $", specString) + str(format(netPay, specFloat))

# print information
print(msg)
