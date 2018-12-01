# Simple CSV to XML Conversion - Python
# by Chalermporn Posoppitukwong
# 

import csv

csvFile = 'color.csv'
xmlFile = 'color.xml'

with open(csvFile) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    data = []
    for row in readCSV:
        color = row[3]
        date = row[0]
        data.append(row)
        dates.append(date)
        colors.append(color)

# Output 
print(dates)
print(colors)
print(data)



# Fuction convert
def convert_row(row):
    return """<color="%s">
    <date-time>%s</date-time>
    <num1>%s</num1>
    <num2>%s</num2>
</color>""" % (row[3], row[0], row[1], row[2])

print ('\n'.join([convert_row(row) for row in data[0:]]))

    
# Write file XML
xmlData = open(xmlFile, 'w')
xmlData.write('<?xml version="1.0" encoding="utf-8"?>' + "\n")
xmlData.write('\n'.join([convert_row(row) for row in data[0:]]))
xmlData.close()