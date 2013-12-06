#!/usr/bin/python

# second mapper to sum the tripplet occurances

import sys

sequences = {}

# input from std in
for line in sys.stdin:
    
    # remove whitespaces
    line = line.strip()
    
    # make split the string into words based on whitespaces 
    tripple, count = line.rsplit('\t',1)
    print '%s\t%s' % (count, tripple)
    
                    
    

