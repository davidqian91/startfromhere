import sys
import re

inputFile = sys.argv[1]
outputFile = sys.argv[2]

file2write = open(outputFile, 'wb')
with open(inputFile, 'rb') as f:
    for line in f:
    	count = 0
    	m = re.split('\W+', line)
    	for w in m:
    		if w != "" and len(w) > 0:
    			count += 1
    	file2write.write(str(count)+'\n')


