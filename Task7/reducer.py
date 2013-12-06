#!/usr/bin/python

# reducer that just prints what it gets, i.e. does nothing really

from operator import itemgetter
import sys

rowIndex = 0
prevRowIndex = 0
row = []
printrow = []

# input from STDIN
for line in sys.stdin: 

    # isolate columnIndex, value pairs  
    rowIndex, t = line.split('\t',1)
    rowIntex = int(rowIndex)
    columnIndex, value = t.split()
    value = int(value)
    columnIndex = int(columnIndex)
    

    # check if we're still dealing with the same row
    if prevRowIndex == rowIndex :
        row.append((columnIndex, value))
    else :
        if prevRowIndex :
            # sort the row vector in order of columns 
            row = sorted(row, key=lambda colIndex: colIndex[0])
            for x in range(0, len(row)):
                (colIndex, val) = row[x]
                printrow.append(val)   
            print ' '.join(map(str, printrow))
        printrow = []    
        row = []
        row.append((columnIndex, value))
        prevRowIndex = rowIndex
        
        
               
if prevRowIndex == rowIndex :
    row = sorted(row, key=lambda colIndex: colIndex[0])
    for x in range(0, len(row)):
        (colIndex, val) = row[x]
        printrow.append(val)
    print ' '.join(map(str, printrow))    
    
    
      


    
            

"""
hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D mapred.text.key.comparator.options=-n -D mapred.reduce.tasks=1 -input /user/s1008380/data/input/part2 -output /user/s1008380/data/output/task7 -mapper mapper.py -file mapper.py -reducer reducer.py -file reducer.py 
 
 """
