# Example input
#s = 'cfgff5d8;4'
s = ''

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    digits = '0123456789'
    try:
        if len(s) == 0:
            raise ValueError('Empty string')
        sum = 0
        for char in s:
            if char in digits:
                sum += int(char)
        return sum

    except ValueError as error:
        print('Error: ' + repr(error))
            