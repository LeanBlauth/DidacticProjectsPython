initialBalance      = 999999
balance = initialBalance
nextBalance         = initialBalance
annualInterestRate  = 0.2
monthlyInterestRate = annualInterestRate/12
monthlyPayment      = 10

lowerBound = initialBalance/12
upperBound = (initialBalance*(1+monthlyInterestRate)**12)/12
average = (lowerBound+upperBound)/2
monthlyPayment = average

while ((balance < -0.1) or (balance > +0.1)):
    unpBalance      = 0
    balance         = initialBalance
    for i in range(12):
        unpBalance = balance - monthlyPayment
        nextBalance = (1+monthlyInterestRate)*unpBalance
        balance = nextBalance
    if (balance < 0):
        upperBound = average
    else:
        lowerBound = average
    average = (lowerBound+upperBound)/2
    monthlyPayment = average
    print("Monthly Payment: " + str(round(monthlyPayment,2)))
    print("Balance: " + str(round(balance,2)))
print("Lowest Payment: " + str(round(monthlyPayment,2)))