import codecs
import re

inFile = codecs.open('full.html', 'r', 'utf-8')
outFile = codecs.open('reduced.html', 'w', 'utf-8')
for line in inFile:
    newLine = re.sub(' align=\"center\" nowrap', '', line)
    newLine = re.sub(' align=\"left\" nowrap', '', newLine)
    newLine = re.sub(' bgcolor=\"#EEEEEE\"', '', newLine)
    newLine = re.sub(' bgcolor=\"#DDDDDD\"', '', newLine)
    newLine = re.sub(' bgcolor=\"#CCCCCC\"', '', newLine)
    newLine = re.sub(' align=\"right\" nowrap', '', newLine)
    newLine = re.sub('<font face=\"courier, monospace\" size=\"-1\">', '', newLine)
    newLine = re.sub('</font>', '', newLine)
    newLine = re.sub(' nowrap', '', newLine)
    newLine = re.sub('<&nbsp', '', newLine)
    outFile.write(newLine)
inFile.close()
outFile.close()
