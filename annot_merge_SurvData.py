import sys

# usage: python annot_merge_SurvData.py input_annotFile.txt output_mergedFile.txt

inputFile = sys.argv[1]
outputFile = sys.argv[2]

f=open(inputFile)
fw=open(outputFile,'w')

header = f.readline()

for line in f:
    lineSplit = line.replace("\n","").split('\t')
    #print lineSplit
    GSE_ID = lineSplit[0]
    GPL_ID = lineSplit[1]
    
    survFile = "./ovs/surv_" + GSE_ID + "-" + GPL_ID + "_SYMBOL_overall_survival.txt"

    f_surv = open(survFile)

    for line_surv in f_surv:
        #lineSurvSplit = line_surv.strip().split('\t')
        wStr = line.replace("\n","") + "\t" + line_surv
        #print wStr
        fw.write(wStr)

    f_surv.close()
fw.close()
f.close()
