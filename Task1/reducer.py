#!/usr/bin/python

# reducer that just prints what it gets, i.e. does nothing really

from operator import itemgetter
import sys




# input from STDIN
for line in sys.stdin :
    
    line = line.strip()
    # get rid of the tab and the 1 at the end
    sentence = line.rsplit('\t',1)
    """
    using sentence, value = line.rsplit('\ t',1) kept returning failed jobs when
    running it over the large dataset due to the \ t 1 not always being present
    accessing with sentence[0] always works,
    """
    
    # write result to std out
    print sentence[0]
    
            

"""
 hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -input /user/s1008380/data/input/part1 -output /user/s1008380/data/output/task1 -mapper mapper.py -file mapper.py -reducer reducer.py -file reducer.py 
 
 """
