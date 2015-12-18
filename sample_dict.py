import os
import sys
import re
import collections

def arrangedict_frmsys(dict, pref, suff):
    # adds a new item in the dictionary from command line
    oldsuf = dict.has_key(pref) # checking if K exists
    if oldsuf == False :        # if new K, add [K,V]
        dict[pref]=suff
    else:
        val = dict.get(pref)    # if key, then append to new V to existing V and add to [K,V]
        val = val + ',' + suff        
        dict[pref]=val    
    return dict


    
def arrangedict():
    fd = open('pg78.txt', "r")
    for line in fd:
        line = line.lower() # for all lines convert to lowercase
        #t = re.sub(r'[_,":-;.]', ' ', line)    
        t = re.sub(r'["\s,.";_:-]', ' ', line)  # strip all extra characters
        t1 = re.split(' ', t)   # split and put in L
        count = 0
        dict_count = 0
        for allc in t1:            
                if allc == '':      # strip away empty strings in L                         
                    t1 = t1[:count] + t1[count+1:]
                    count = count - 1
                count = count + 1           
        rpt = 0
        
        for ind in t1:        # for all elements in L
            if dict_count == 0:            # first element is skipped
                pref = ind
                dict_count = dict_count + 1
            else:
                
                if rpt == 1:    # if key, then append to new V to existing V and add to [K,V]
                    
                    rpt = 0
                    ind1 = ind1 + ',' + ind
                    dict[pref] = ind1                
                    pref = ind
                    ind1 = '' 
                if ind in dict:   # if K, need to save for next iteration  . V is always K in (current iteration)-1, so checking here itself and flagging repeat
                    ind1 = dict.get(ind)                
                    rpt = 1
                    dict[pref] = ind
                    pref = ind
                else:           # if new K, add [K,V]
                    dict[pref] = ind
                    pref = ind           
    return dict

if __name__ == '__main__':
    dict = {}
    # adding all elements of file pg78.txt to the dictionary
    
    dict = arrangedict()
    # optionally you can print all arg after it adds just to check
    #print dict

    print "\n\nEnter words to see the next potential match of word(s)... \n\n"
    while 1:
        
        try:            
            line = sys.stdin.readline()
        except KeyboardInterrupt:
            break

        if not line:
            break
        
        t = re.sub('\\n', '', line)
        os.system('CLS')
        
        print "\n\nYou entered ... " , line        
        val  = dict.get(t)        
        if(val):
            print t , "-->", val            
            print "\n\nDo you want to enter a new substring to this prefix?"
            print "If yes, press suffix, else press enter\n\n"
            line3 = sys.stdin.readline()
            istrng = re.sub('\\n', '', line3)            
            if line3 != '' :
                suff2 = re.sub('\\n', '', line3)
                dict = arrangedict_frmsys(dict, t, suff2)
                os.system('CLS')
                val2 = dict.get(t)
                print "\n\n", t , "-->", val2            
                
            print "\n\nEnter more words to match or Ctrl+C to quit\n\n"
        else:
            print " \n\n This is a new string not in dictionary... Enter the next string to add to dictionary\n\n"

            line2 = sys.stdin.readline()
            pref = re.sub('\\n', '', line)
            suff = re.sub('\\n', '', line2)
            dict = arrangedict_frmsys(dict, pref, suff)
            os.system('CLS')
            print " \n\nNew subset of strings added to dictionary\n\n", pref , "-->" , suff
            print "\n\nEnter more words to predict potential substrings or Ctrl+C to quit\n\n"
            
