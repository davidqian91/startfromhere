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
        print(row)
        s = "INSERT INTO tramstop VALUES("
        s += "'"+row[0].strip() + "',"
        s += "SDO_GEOMETRY("
        s += "2003,"
        s += "NULL,"
        s += "NULL,"
        s += "SDO_ELEM_INFO_ARRAY(1,1003,4),"
        s += "SDO_ORDINATE_ARRAY("
        x = int(row[1])
        y = int(row[2])
        r = int(row[3])
        s += str(x+r) + "," + str(y) + ","
        s += str(x) + "," + str(y+r) + ","
        s += str(x-r) + "," + str(y)
        s += ")));"
        file2write.write(s+"\n")
