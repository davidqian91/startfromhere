## csv hanlder
## find date type in format ##/##/##
## replace single digit # with 0#
## takes filename as a command line parameter
import csv
import sys

filename = sys.argv[1]
#tablename = sys.argv[2]
file2write = open(filename+".sql", 'wb')
with open(filename, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        #print(row)
        str = "INSERT INTO student VALUES("
        str += "'"+row[0].strip() + "',"
        str += "SDO_GEOMETRY("
        str += "2001,"
        str += "NULL,"
        str += "SDO_POINT_TYPE("
        str += row[1]+","+row[2]
        str += ", NULL),"
        str += "NULL,"
        str += "NULL));"
        file2write.write(str+"\n")
