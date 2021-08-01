# Example input
aDict = {
    5 : 8,
    2 : 1,
    9 : 78,
    6: 65,
    7: 65,
    8: 65,
    1000: 65,
    1: 65}

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    
    def sorter(L):
        '''
        L: a list
        '''
        index = len(L)-1
        while (index > 0):
            if (L[index] < L[index-1]):
                (L[index], L[index-1]) = (L[index-1], L[index])
                index = len(L)-1
            else:
                index -= 1
        return L
    
    keyList = []
    for key, value in aDict.items():
        if value == target:
            keyList.append(key)
    
    return sorter(keyList)
    