#!/usr/bin/python

# reducer that just prints what it gets, i.e. does nothing really

from operator import itemgetter
import sys

wordCount = 0
lineCount = 0


# input from STDIN
for line in sys.stdin :

    line = line.strip()
    
    # get rid of the tab and the 1 at the end
    words, sentences = line.rsplit('\t',1)

    # convert the strings into ints
    sentences = int(sentences)
    words = int(words)
    
    # add number of words and lines to their counts
    wordCount += words
    lineCount += sentences
    
# write result to std out
print '%s %s' % (wordCount, lineCount)
    
            

"""
 hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -input /user/s1008380/data/input/part1 -output /user/s1008380/data/output/task3 -mapper mapper.py -file mapper.py -reducer reducer.py -file reducer.py -D mapred.reduce.tasks=1
 
 """
