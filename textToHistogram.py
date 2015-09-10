#1/usr/bin/python3
#
#
# by: Francis Kessie  
#     
#

"""
Process text from input file and implements a histogram creation algorithm. 


This program takes input text file and counts all text in file.
symbols and punctuation marks are ignored. The program returns a table
with word size and corresponding word counts and implements a histogram creation
algorithm to draw a histogram of word size vrs word count.
"""

import string
import sys

def file_processor(myfile):
    """
    reads and process input file and also removes all 
    punctuation symbols from text   
    """    
    with open(myfile, "r") as inp:
        filea = inp.read()
    for punc in string.punctuation:      
        filea = filea.replace(punc, "")
    return filea

def get_dict(wordlist, x):
    """
    creates a dict with count of text as key and 
    and word size as values
    """
    mylist = []
    mydict = {}
    for a, b in wordlist:
        if b == x:
            mylist.append(a)
            mydict[x] = len(mylist)
    return mydict
            

def get_countlist(words):
    """
    returns a list containing all possible word sizes in text
    """
    count_set = set()
    for word in words:
        count_set.add(len(word))
        countlist = sorted(count_set)
    return countlist

def histogram(dictx):
    """draw a histogram of word count and wordsize"""
    #Get maximum x and Y values, plus two to help graph display
    maxi_xval = max(dictx.keys())+2
    maxi_yval = max(dictx.values())+2
                
   #draw histogram by row            
    for inp in range(400, 0, -20):
        ###
        
        if inp%100 == 0:
            draw = str(inp)+"-|"
        else:
            draw = '    |'
                       
        for ind in range(1, maxi_xval):
            if ind in dictx.keys() and dictx[ind] >= inp:
                draw += '***'
            else:
                draw += '   '
        print("{1} {0}".format(draw, ' '))

    #format and print x-axis
    x_axis = '      0--+-'
    for i in range(0, maxi_xval+2):
        x_axis += '-+-'
    print(x_axis)
                
    #format and print scale of x-axis
    x_scale = '      '
    for j in range(1, maxi_xval):
        space = ' '
        if j < 10:
            space = space + ' '
        x_scale = x_scale + space
        x_scale = x_scale + str(j)
    print("{2}{0}{1}".format('', x_scale, ' '))
 
if __name__ == "__main__":
    
    # Prompt user if no correct input supplied
    # process file and store text with corresponding count as list of tuples
    while True:        
        try:
            mytextfile = sys.argv[1]   
            words = file_processor(mytextfile).split() 
            wordlist = [] 
                     
            for word in words:
                wordbin = tuple([word, len(word)])
                wordlist.append(wordbin) 
    
            #print table to screen in required format        
            print("Length", '\t', "Count")    
            countlist = get_countlist(words)           
    
            dictb = {}
            for values in countlist:
                table = get_dict(wordlist, values)
                for key, value in table.items(): 
                     dictb[key] = value      
                     print(key, '\t', value)
           
            print(" ")
            print(" ")
            
            #draw histogram
            histogram(dictb)
            break
        
        except IndexError:
            print('Text file not supplied, (Type script name and name of text file(e.g textToHistogram.py sample_text.txt)')
            break
        except FileNotFoundError:
            print('Cannot find text file, (Check and Provide correct text file name!)')
            break
