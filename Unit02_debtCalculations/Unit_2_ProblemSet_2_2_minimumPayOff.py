initialBalance      = 3926
nextBalance         = initialBalance
annualInterestRate  = 0.2
monthlyPayment      = 10

while (nextBalance > 0):
    monthlyPayment += 10
    unpBalance      = 0
    balance         = initialBalance
    for i in range(12):
        unpBalance = balance - monthlyPayment
        nextBalance = (1+annualInterestRate/12)*unpBalance
        balance = nextBalance
    print("Remaining Balance: " + str(round(nextBalance,2)))
print("Lowest Payment: " + str(round(monthlyPayment,2)))