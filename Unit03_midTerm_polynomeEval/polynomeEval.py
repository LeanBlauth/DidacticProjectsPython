# Example input
L = [1,2,3,4]
x = 10

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
    def poly(base):
        """ base: int
        Returns the polynome valuation at given base """
    
        LSP = len(L)-1 # Least Significant Place
        place = LSP
        sum = 0
        while(place >= 0):
            sum += L[place]*base**(LSP - place)
            place -= 1
        return sum
    return poly

general_poly(L)(x)