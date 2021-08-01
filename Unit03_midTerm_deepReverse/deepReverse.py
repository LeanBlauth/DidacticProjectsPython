# Example input
L = [[1, 2], [3, 4], [5, 6, 7]]

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L.
    It does not return anything.
    """
    
    def reverse(L):
        rev = []
        for element in reversed(L):
            rev.append(element)
        return rev

    for index in range(len(L)):
        L[index] = reverse(L[index])
    L = reverse(L)