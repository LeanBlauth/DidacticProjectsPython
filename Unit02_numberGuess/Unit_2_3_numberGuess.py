lowerBound = 0
upperBound = 100
guess = (upperBound + lowerBound)/2
hint = ''

print("Please think of a number between \
      " + str(lowerBound) + " and " + str(upperBound))
while (hint != 'c'):
    print("\n Is your secret number " + str(int(guess)) + " ?")
    hint = input("Enter 'h' to indicate the guess is too high.\
                  Enter 'l' to indicate the guess is too low.\
                  Enter 'c' to indicate I guessed correctly: ")
    if (hint == 'h'):   upperBound = guess
    elif (hint == 'l'): lowerBound = guess
    elif (hint == 'c'): pass
    else:               print("Sorry, I did not understand your input.")
    if (hint != 'c'):   guess = int((upperBound + lowerBound)/2)
print("\n Game over. Your secret number was: " + str(int(guess)))
    
        