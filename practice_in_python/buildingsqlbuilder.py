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
        str = "INSERT INTO building VALUES("
        str += "'"+row[0].strip() + "',"
        str += "'"+row[1].strip() + "',"
        str += "SDO_GEOMETRY("
        str += "2003,"
        str += "NULL,"
        str += "NULL,"
        str += "SDO_ELEM_INFO_ARRAY(1,1003,1),"
        str += "SDO_ORDINATE_ARRAY("
        for k in range(3, len(row), 1):
            str += row[k]+','
        str += row[3]+','+row[4]
        str += ")));"
        file2write.write(str+"\n")
