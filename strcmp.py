# searches for palindromes
# removes blank spaces in all strings before palindrome search


def rightlen(str):
    print str
    blnkindx = str.find(' ')    
    y = str[0:blnkindx] + str[blnkindx+1:len(str)]    
    fndblnkspace = y.find(' ')
    if fndblnkspace!=-1:
        y = rightlen(y) 
        return y
    else:
        return y

    
def alternstr(strx):
    stry = ''
    letter = strx[0]
    stry = strx[1:]+letter
    return stry
    
fin = open('words1.txt')

succ = -1
for line in fin:   
    
    reversestr = ''
    fndblnkspace = line.find(' ')
    if fndblnkspace!=-1:
        retline = (rightlen(line))
    

    for eachchar in retline:
        reversestr = eachchar + reversestr

    
    
    loop = len(retline)    
    counter = 0
    altstrx = retline
    
    succ = 0
    while (counter < loop):             
        altstry = alternstr(altstrx)        
        altstrx = altstry        
        counter+=1

        if altstry == reversestr:            
            succ = 1
            print line + " is a palindrome"
                
    if succ == 0:
        print line + " is not a palindrome"

    
    
        
        
