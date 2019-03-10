#partie V.2

import sys 
import re


lineNb = 1 #used in debug

corresFile = open("corresDict.txt")
corresDict = {}

dictLines = corresFile.readlines()

for i in range(len(dictLines)):
    entite = dictLines[i].split('\t')
    corresDict[entite[0]] = entite[1]

inputFile = open(sys.argv[1],"r")
outputFile = open(sys.argv[2],"w")

lignes = inputFile.readlines()

for i in range(len(lines)):
    lignes[i] = lignes[i].split('\t')

    if lines[i] != '\n':
        
        info = lines[i].strip().split("\t")

        w, se = info[1], info[5]

        w = re.sub('\s+', 'Espace', w)

        outputFile.write(w + "/" + corresDict[se] + " ")
    else:
        outputFile.write("\n")
    lineNb += 1