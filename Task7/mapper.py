#!/usr/bin/python

# mapper to count words per line and return that

import sys



# input from std in
for line in sys.stdin:

    # remove whitespaces
    line = line.strip()
    # make split the string into a rowIndex and the row values
    rowIndex, values = line.split('\t', 1)
    values = values.split()

    # with the columnIndex as key, they'll arrive at the reducer in groups of rows of the new transposed matrix
    for columnIndex in range(0, len(values)):
        print '%s\t%s %s' % (columnIndex, rowIndex, values[columnIndex])   
                
    

      
    

  
    
        
        
        
    
