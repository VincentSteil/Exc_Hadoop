#!/usr/bin/python

# mapper to count words per line and return that

import sys

wordCount = 0
lineCount = 0

# input from std in
for line in sys.stdin:

    # remove whitespaces
    line = line.strip()
    
    # make split the string into words based on whitespaces (as wc does)
    words = line.split()
    
    # update word counter
    wordCount += len(words)
    
    # update line counter
    lineCount += 1
    
    
    
# write the number of words and lines to std out
# this only sends out one tuple of wordCount and lineCount per shard to the reducers
print '%s\t%s' % (wordCount, lineCount)
  
    
        
        
        
    
