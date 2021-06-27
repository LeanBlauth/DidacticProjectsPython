def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
        
    prod = 1
    for i in range(exp):
        prod *= base
    return prod