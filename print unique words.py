import string
import random

def skipheader(fd):
     for line in fd:
        if line.startswith('*END*THE SMALL PRINT!'):
            break

def cleanvalues (line, datadict):
    line.replace ('-', ' ')
    for word in line.split():        
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        datadict[word]=datadict.get(word,0) +1


def readfile_minusheader(filename):
    datadict = {}
    fd = file(filename)
    for line in fd:
        cleanvalues(line, datadict)
    return datadict

def uniquewords(datadict):
    return len(datadict)

def totalwords(datadict):
    return sum(datadict.values())

if __name__ == '__main__':
    
    histogram = readfile_minusheader('emma.txt')  

    print 'Total Words in Emma ' , totalwords(histogram)
    print 'Unique Words ', uniquewords(histogram)

    t =[]
    for key,value in histogram.items():
        t.append((value,key))

    t.sort()
    t.reverse()

    for count, word in t[:10]:
        print word , '  is printed ' , count , '    times'  
    

        
