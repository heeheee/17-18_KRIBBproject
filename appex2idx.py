import sys
from numpy import *


# usage: python appex2idx.py input_appexFile.txt output_idxFile.txt

inputFile = sys.argv[1]
outputFile = sys.argv[2]

f=open(inputFile)

header_GSMID = f.readline()
header_Time = f.readline()
header_Censor = f.readline()

#headerSplit_GSMID = header_GSMID.strip().split('\t')
#headerSplit_Time = header_Time.strip().split('\t')
#headerSplit_Censor = header_Censor.strip().split('\t')

#headerSplit_GSMID.pop(0)
#headerSplit_Time.pop(0)
#headerSplit_Censor.pop(0)

dicIndex = {}

for line in f:
    lineSplit = line.strip().split('\t')
    geneSymbol = lineSplit[0]
    lineSplit.pop(0)
    listExp = map(float,lineSplit)
    expMedian = median(listExp)
    listIndex = []

    for exp in listExp:
        if(exp > expMedian):
            listIndex.append("1")
        else:
            listIndex.append("0")

    checkAllSameIdx = 1
    firstIdx = listIndex[0]

    for idx in listIndex:
        if(idx != firstIdx):
            checkAllSameIdx = 0
                
    if(checkAllSameIdx == 0):
        dicIndex[geneSymbol] = listIndex

f.close()

fw = open(outputFile, 'w')

fw.write(header_GSMID)
fw.write(header_Censor)
fw.write(header_Time)

for key in dicIndex:
    wStr = key
    for idx in dicIndex[key]:
        wStr = wStr + "\t" + idx

    wStr = wStr + "\n"
    fw.write(wStr)
    
fw.close()
