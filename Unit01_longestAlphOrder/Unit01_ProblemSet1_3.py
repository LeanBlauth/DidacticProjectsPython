s = "abcabcegpzbaabcdefgh"
s += " "
alphabet = [" ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"];
currentStreak = s[0]
maxLen = 0
maxStreak = ""

for x in range(len(s)-1):
    if alphabet.index(s[x+1]) >= alphabet.index(s[x]):
        currentStreak += s[x+1]
    else:
        if len(currentStreak) > maxLen:
            maxLen = len(currentStreak)
            maxStreak = currentStreak
        currentStreak = s[x+1]

print("Longest substring in alphabetical order is: " + maxStreak)
