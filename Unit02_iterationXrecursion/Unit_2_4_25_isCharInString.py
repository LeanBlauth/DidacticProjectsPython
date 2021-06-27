def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    strLen = len(aStr)
    middle = int(strLen/2)
    if (aStr == ''):
        return False
    elif (aStr[middle] == char):
        return True
    else:
        if(char > aStr[middle]):
            aStr = aStr[middle+1:]
        else:
            aStr = aStr[:middle]
        return isIn(char, aStr)