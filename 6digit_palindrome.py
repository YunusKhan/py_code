# prints numbers bet 10000 and 99999 which are palindromes

val = 100000
count = 0

while val <= 999999:

    val = val+1

    strval = str(val)

    revval = ''
    for letter in strval:
        revval = letter + revval
        
    if strval == revval:
        count = count + 1
        print strval
    
print "total # of palindrome numbers between 10000 and 999999 is ", + count
