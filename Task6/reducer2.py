#!/usr/bin/python

# reducer that combines the count of 3 word tripplets

from operator import itemgetter
import sys

sequences = []



# input from STDIN
for line in sys.stdin :
    line = line.strip()
    count, tripple = line.split('\t',1)
    # convert the string counts into ints
    count = int(count)
    sequences.append((count, tripple))
        
        


# sort the sequences by number of occurrences    
sequences = sorted(sequences, key=lambda count: count[0], reverse=True)

for i in range(0,20):
    count, sequence = sequences[i] 
    print '%s\t%s' % (sequence, count)

    
            

"""
hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -D mapred.output.key.comparator.class=org.apache.hadoop.mapred.lib.KeyFieldBasedComparator -D mapred.text.key.comparator.options=-n -D mapred.reduce.tasks=1 -input /user/s1008380/data/output/task6 -output /user/s1008380/data/output/task6/finaloutput -mapper mapper2.py -file mapper2.py -reducer reducer2.py -file reducer2.py
 
 """
