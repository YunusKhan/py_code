# find 3 pairs of 2 consecutive same letters
# test

def searchdoubles(line):
    index = 0
    cont = 0
    cont1 = 0
    cont2 = 0
    cont3 = 0
    linelen = len(line)    
    
    for letter in line:
        if index > linelen-2:            
            break

        letter2 = line[index+1]
        index += 1

        if cont1 == 1:
            if cont2 == 1:
                if cont3 == 1:                          
                    print line
                    return
                    
                    
        if cont1 ==1 :
            if cont2 == 1:
                if cont3 != 1:
                    if letter==letter2:
                        cont3 = 1
        if cont1 ==1 :
            if cont2 != 1:                
                if letter==letter2:
                    cont2 = 1                    

        if cont1 !=1 :
            if letter==letter2:
                cont1 = 1

fin = open('word.txt')

print " list of words which have a triple sets of same consecutive characters "
result = ''
for line in fin:
    searchdoubles(line)
