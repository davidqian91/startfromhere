## csv hanlder
## find date type in format ##/##/##
## replace single digit # with 0#
## takes filename as a command line parameter
import csv
import sys
import re


def myReplace(matchObj):
    if int(matchObj.group(0)) < 10:
        return "0"+matchObj.group(0)
    else:
        return matchObj.group(0)


filename = sys.argv[1]
file2write = open(filename+".bak", 'wb')
writer = csv.writer(file2write)
with open(filename, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        #print(row)
        for i in range(len(row)):
            if re.search('^\d+/\d+/\d+$', row[i]):
                m = re.sub('\d{1,2}', myReplace, row[i])
                row[i] = m
        #print(row)
        writer.writerow(row)
