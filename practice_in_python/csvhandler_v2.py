## csv hanlder
## find date type in format ##/##/##
## replace single digit # with 0#
## takes filename as a command line parameter
import csv
import sys
import re

filename = sys.argv[1]
file2write = open(filename+".bak", 'wb')
writer = csv.writer(file2write)
with open(filename, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        #print(row)
        for i in range(len(row)):
            m = re.search('^(\d+)/(\d+)/(\d+)$', row[i])
            if m:
                year = m.group(3)
                if int(year) > 20:
                    year = "19"+year
                else:
                    year = "20"+year
                month = m.group(1)
                day = m.group(2)
                if int(month) < 10:
                    month = "0"+month
                if int(day) < 10:
                    day = "0"+day
                row[i] = year+"-"+month+"-"+day
        print(row)
        writer.writerow(row)
