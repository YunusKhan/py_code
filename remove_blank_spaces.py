# calculates lenstr > 20 discounting blank spaces as length.

def rightlen(str):    
    blnkindx = str.find(' ')    
    y = str[0:blnkindx] + str[blnkindx+1:len(str)]    
    fndblnkspace = y.find(' ')
    if fndblnkspace!=-1:
        y = rightlen(y)      

    print y
    return y
        
    

fin = open('words1.txt')

for line in fin:
    #fndblnkspace = line.find(' ')    
    retstr = (rightlen(line))
    print "..."
    print retstr
