balance             = 42
annualInterestRate  = 0.2
monthlyPaymentRate  = 0.04
unpBalance = 0
for i in range(12):
    unpBalance = (1-monthlyPaymentRate)*balance
    nextBalance = (1+annualInterestRate/12)*unpBalance
    print("Month " + str(i+1) + " Remaining Balance: " \
          + str(round(nextBalance,2)))
    balance = nextBalance
print("Remaining Balance: " + str(round(nextBalance,2)))