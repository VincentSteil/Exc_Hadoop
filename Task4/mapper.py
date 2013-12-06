#!/usr/bin/python

# mapper to probabilistically count words per line 

import sys
import random

# initialise rng
random.seed()

wordCount = 0

# lineCount is the PROBABILISTIC counter (2^-lineCount etc)
lineCount = 0

# input from std in
for line in sys.stdin:
    # ** is power of and random.random generates a uniform random var on [0,1]
    if (float(2**(-lineCount)) > random.random()): 
        # remove whitespaces
        line = line.strip()
    
        # make split the string into words based on whitespaces (as wc does)
        words = line.split()
    
        # update word counter
        # since we only update the wordCounter when we update the lineCounter, we get the same size savings
        wordCount += len(words)
    
        # update line counter
        lineCount += 1
    
    
    
# write the number of words and lines to std out
# this only sends out one tuple of wordCount and lineCount per shard to the reducers
# remember, lineCount and wordCount are log scaled
print '%s\t%s' % (wordCount, lineCount)
  
    
        
        
        
    
