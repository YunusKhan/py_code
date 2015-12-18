import os
import sys
import re
import collections

def revcounter(dict): 
    for ind2 in dict:        
        val2 = dict.get(ind2)        
        key2 = revdict.has_key(val2)       #check if key exists 
        if not(key2):   # if first occurence add to reverse dict
            revdict[val2] = ind2
        else:   # if occurence already exists, append the word and add to value
            ind3 = revdict[val2]
            ind3 = ind3 + ' , ' +  ind2
            revdict[val2] = ind3
            
    rev = collections.OrderedDict(sorted(revdict.items(), reverse = True))         
    return rev
                
    

    
def addcounter(): 
    fd = open('pg78.txt', "r")
    for line in fd:
        line = line.lower() # for all lines convert to lowercase
        #t = re.sub(r'[_,":-;.]', ' ', line)    
        t = re.sub(r'["\s,.";_:-]', ' ', line)  # strip all extra characters
        t1 = re.split(' ', t)   # split and put in L
        count = 0        
        for allc in t1:            
                if allc == '':      # strip away empty strings in L                         
                    t1 = t1[:count] + t1[count+1:]
                    count = count - 1
                count = count + 1           
        rpt = 0
        
        for ind in t1:
            if dict.get(ind) >= 1:
                val = dict.get(ind) + 1
                dict[ind] = val
            else:
                dict[ind] = 1
    return dict

if __name__ == '__main__':
    dict = {}
    revdict = {}
    # adding all elements of file pg78.txt to the dictionary

    # first build the dictionary
    dict = addcounter() 

    # build a reverse dictionary on dictionary
    revdict = revcounter(dict)  
    
    os.system('CLS')
    print ' \n Top 15 word occurences ...'   
    count = 0
    for ind3 in revdict:
        print ind3 , ' : ' , revdict[ind3]
        count = count + 1
        if count > 15:
            break
        
            
        




