import os
import sys
import re
import collections

def arrangedict_frmsys(dict, pref, suff):    
    oldsuf = dict.has_key(pref)
    print oldsuf
    if oldsuf == False :
        dict[pref]=suff
    else:
        val = dict.get(pref)
        val = val + ',' + suff
        print val
        dict[pref]=val
    
    return dict


    
def arrangedict():
    fd = open('pg78.txt', "r")
    for line in fd:
        line = line.lower()
        #t = re.sub(r'[_,":-;.]', ' ', line)    
        t = re.sub(r'["\s,.";_:-]', ' ', line)
        t1 = re.split(' ', t)
        count = 0
        dict_count = 0
        for allc in t1:            
                if allc == '':                               
                    t1 = t1[:count] + t1[count+1:]
                    count = count - 1
                count = count + 1           
        rpt = 0
        
        for ind in t1:        
            if dict_count == 0:            
                pref = ind
                dict_count = dict_count + 1
            else:
                
                if rpt == 1:
                    
                    rpt = 0
                    ind1 = ind1 + ',' + ind
                    dict[pref] = ind1                
                    pref = ind
                    ind1 = '' 
                if ind in dict:               
                    ind1 = dict.get(ind)                
                    rpt = 1
                    dict[pref] = ind
                    pref = ind
                else:
                    dict[pref] = ind
                    pref = ind           
    return dict

if __name__ == '__main__':
    dict = {}
    dict = arrangedict()
    print "\n\nEnter words to see the next potential substring... \n\n"
    while 1:
        
        try:            
            line = sys.stdin.readline()
        except KeyboardInterrupt:
            break

        if not line:
            break
        
        t = re.sub('\\n', '', line)
        #os.system('CLS')
        
        print "\n\nYou entered ... \n\n"
        print line
        val  = dict.get(t)        
        
        
        
        if(val):
            print " \n\nNext set of probable words are .. \n\n "
            print val
            print "\n\nDo you want to enter a new substring to this prefix?"
            print "If yes, press 1 else press enter\n\n"
            line3 = sys.stdin.readline()
            istrng = re.sub('\\n', '', line3)
            line3=''
            if int(istrng) == 1:
                print "\n\n .. Enter the new suffix \n\n"
                line4 = sys.stdin.readline()
                suff2 = re.sub('\\n', '', line4)
                line4=''
                dict = arrangedict_frmsys(dict, t, suff2)
            print "\n\nEnter more words to match or Ctrl+C to quit\n\n"
        else:
            print " \n\n This is a new string ... Enter the next string to add to dictionary\n\n"

            line2 = sys.stdin.readline()
            pref = re.sub('\\n', '', line)
            suff = re.sub('\\n', '', line2)
            dict = arrangedict_frmsys(dict, pref, suff)
            line2 = ''
            line1 = ''
            print " \n\nNew subset of strings added to dictionary\n\n"
            print "\n\nEnter more words to match or Ctrl+C to quit\n\n"
            
