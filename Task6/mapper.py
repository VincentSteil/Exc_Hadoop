#!/usr/bin/python

# mapper to count number of 3 word trippletts

import sys

sequences = {}


# input from std in
for line in sys.stdin:

    # remove whitespaces
    line = line.strip()
    
    # make split the string into words based on whitespaces 
    words = line.split()
    
    # if there are less than 3 words, there can be no tripple
    if len(words) >= 3:
        for i in range(0, (len(words)-3)):
            tripple = (words[i], words[i+1], words[i+2])
            # add tripple to dict or update count
            if tripple in sequences:
                sequences[tripple] += 1
            else:
                sequences[tripple] = 1
                    
    
for tripple, count in sequences.items():
    # write the tripples and their counts to stdout
    print '%s %s %s\t%s' % (tripple[0], tripple[1], tripple[2], count)    
    

  
    
        
        
        
    
