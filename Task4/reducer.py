#!/usr/bin/python

# reducer that just prints what it gets, i.e. does nothing really

from operator import itemgetter
import sys

wordCount = 0
wordsPerLine = 0
lineCountSamples = 0
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
    # lineCountSamples is in the log domain and used to later get words/line
    lineCountSamples += sentences
    # bring sentences back into linear domain
    lineCount += (2**sentences) -1

"""
Currently, we have the number of words for a total of lineCount lines. Since we want to extrapolate from lineCount, we need to get the number of words per line and bring that back after an updated lineCount
Check for 0 division, as a reducer with no data throws an error here
"""
if(lineCount > 0):
    wordsPerLine = float(float(wordCount) / float(lineCountSamples))
    """
    scale lineCount back into the linear domain and scale wordCount accordingly
    """
    wordCount = int(wordsPerLine * lineCount)

    
# write result to std out
print '%s %s' % (wordCount, lineCount)
    
            

"""
 hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar -input /user/s1008380/data/input/part1 -output /user/s1008380/data/output/task4 -mapper mapper.py -file mapper.py -reducer reducer.py -file reducer.py -D mapred.reduce.tasks=1
 
 """
