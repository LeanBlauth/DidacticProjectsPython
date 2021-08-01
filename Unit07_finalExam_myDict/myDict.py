class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ constructor """
        self.myList = []
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        if self.hasKey(k):
            for e in self.myList:
                if e[0] == k:
                    e[1] = v
        else:
            self.myList.append([k,v])
        
    def getval(self, k):
        """ k, immutable object  """
        try:
            if not self.hasKey(k):  raise KeyError(str(k))
            else:
                for e in self.myList:
                    if e[0] == k:   return e[1]
        except KeyError as error:
            print(repr(error))
        
    def delete(self, k):
        """ k, immutable object """   
        try:
            if not self.hasKey(k):  raise KeyError(str(k))
            else:
                temp = []
                for e in self.myList:
                    if e[0] != k:   temp.append(e)
                    else: pass
                self.myList = temp
        except KeyError as error:
            print(repr(error))
    
    def hasKey(self, k):
        for e in self.myList:
            if e[0] == k:
                return True
        return False