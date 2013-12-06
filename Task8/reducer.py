#!/usr/bin/python

# reducer that just prints what it gets, i.e. does nothing really

from operator import itemgetter
import sys

prevStudentID = 0
studentID = 0
classes = []
name = ""

# input from STDIN
for line in sys.stdin: 

    # isolate columnIndex, value pairs  
    studentID, cols = line.split('\t',1)
    print studentID
    print cols
    if prevStudentID == studentID :
        if (len(cols) == 1):
            name = cols[0]
        elif (len(cols) == 2):
            classes.append((cols[0], cols[1]))
    else :
        if prevStudentID :
            # write result to std out
            s2 = " ".join(str(x) for x in classes)
            s = '%s-->%s' % (name, s2)
        classes = []
        name = ""
        prevStudentID = studentID
        if (len(cols) == 1):
            name = cols[0]
        elif (len(cols) == 2):
            classes.append((cols[0], cols[1]))
        
if prevStudentID == studentID :
    s2 = " ".join(str(x) for x in classes)
    s = '%s-->%s' % (name, s2)
    print s
    
        
             
        
        
    
            

"""
hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D mapred.text.key.comparator.options=-n -input /user/s1008380/data/input/part3 -output /user/s1008380/data/output/task8 -mapper mapper.py -file mapper.py -reducer reducer.py -file reducer.py 
 
 """
