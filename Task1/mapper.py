#!/usr/bin/python

# mapper to convert strings to upper case

import sys

# input from std in
for line in sys.stdin:

    # remove whitespaces
    line = line.strip()
    
    # make the string upper case
    upperString = line.upper()
    
    # write the results to std out
    print '%s\t%s' % (upperString, 1)
    
    
        
        
        
    
