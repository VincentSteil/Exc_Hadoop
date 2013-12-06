#!/usr/bin/python

# mapper to count words per line and return that

import sys



# input from std in
for line in sys.stdin:

    # remove whitespaces
    line = line.strip()
    # make split the string into columns
    columns = line.split()
    
    if(columns[0] == 'student'):
        print '%s\t%s' % (columns[1], columns[2])
    elif(columns[0] == 'mark'):
        print '%s\t%s %s' % (columns[2], columns[1], columns[3])

          
    

      
    

  
    
        
        
        
    
