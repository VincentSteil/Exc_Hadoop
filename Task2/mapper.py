#!/usr/bin/python

# mapper to deduplicate data

import sys


sentences = set()

# input from std in
for line in sys.stdin:

    # remove whitespaces
    line = line.strip()
    
    # add lines to set to deduplicate within a shard (sets deduplicate automatically)
    sentences.add(line)

for sentence in sentences:
    
    # write the unique lines to std out
    print '%s\t%s' % (sentence, 1)
    
    """
    hadoop hashes over the keys (sentence). This results in the same sentences going to the same reducers we can thus confidently do the same thing there, as we did in this mapper
    """
    
        
        
        
    
