#!/usr/bin/python

# reducer that combines the count of 3 word tripplets

from operator import itemgetter
import sys

sequences = {}

prevTripple = ""
countTotal = 0
tripple = ""

# input from STDIN
for line in sys.stdin :

    line = line.strip()
    
    # get rid of the tab and the 1 at the end
    tripple, count = line.rsplit('\t',1)

    # convert the string counts into ints
    count = int(count)
    
    if prevTripple == tripple :
        countTotal += count
    else :
        if prevTripple :
            print '%s\t%s' % (prevTripple, countTotal)
        countTotal = count
        prevTripple = tripple
        
if prevTripple == tripple :
    print '%s\t%s' % (prevTripple, countTotal)

    
            

"""
 hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -input /user/s1008380/data/output/task2 -output /user/s1008380/data/output/task5 -mapper mapper.py -file mapper.py -reducer reducer.py -file reducer.py 
 
 """
