s1 = 'dead'
s2 = 'beefbeef'

def laceStringsRecur(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    def helpLaceStrings(s1, s2, out):
        if s1 == '':
            bait = True
        if s2 == '':
            return out if s1 == '' else helpLaceStrings(s1[1:], '', out+s1[0])
        else:
            return helpLaceStrings('', s2[1:], out+s2[0]) if s1 == '' else helpLaceStrings(s1[1:], s2[1:], out+s1[0]+s2[0])
    return helpLaceStrings(s1, s2, '')