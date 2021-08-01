# Example input
aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    keyList = []
    for key in aDict:
        keyList.append(key)
    
    for key1, value1 in aDict.items():
        for key2, value2 in aDict.items():
            if key1 == key2:
                pass
            elif value1 == value2:
                if key1 in keyList: keyList.remove(key1)
                if key2 in keyList: keyList.remove(key2)
    keyList.sort()
    return keyList    
    
print(uniqueValues(aDict))