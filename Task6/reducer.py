#!/usr/bin/python

# reducer that combines the count of 3 word tripplets

from operator import itemgetter
import sys

sequences = []

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
    
    if prevTripple == tripple:
        countTotal += count
    else:
        if prevTripple:
            # use countTotal as key in dict to sort it later
            sequences.append((countTotal, prevTripple))
        countTotal = count
        prevTripple = tripple
        
if prevTripple == tripple:
    sequences.append((countTotal, prevTripple))

# sort the sequences by number of occurrences    
sequences = sorted(sequences, key=lambda count: count[0], reverse=True)

for i in range(0,19):
    count, sequence = sequences[i] 
    print '%s\t%s' % (sequence, count)

    
            

"""
hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -D mapred.reduce.tasks=1 -input /user/s1008380/data/output/task2 -output /user/s1008380/data/output/task6 -mapper mapper.py -file mapper.py -reducer reducer.py -file reducer.py 
 
 """
