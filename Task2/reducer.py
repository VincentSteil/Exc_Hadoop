#!/usr/bin/python

# reducer that deduplicates all incoming lines

from operator import itemgetter
import sys


sentences = set()

# input from STDIN
for line in sys.stdin :
    
    line = line.strip()
    # get rid of the tab and the 1 at the end
    line = line.rsplit('\t',1)
    """
    using sentence, value = line.rsplit('\ t',1) kept returning failed jobs when
    running it over the large dataset due to the \ t 1 not always being present
    accessing with sentence[0] always works,
    """
    # add line to set to deduplicate
    sentences.add(line[0])
    
for sentence in sentences:    
    # write unique sentences to std out
    print sentence
    
            

"""
 hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -input /user/s1008380/data/output/task1 -output /user/s1008380/data/output/task2 -mapper mapper.py -file mapper.py -reducer reducer.py -file reducer.py 
 
 """
