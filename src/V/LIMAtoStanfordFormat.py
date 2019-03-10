#partie V.2
import sys 
import re

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
    if lines[i] != '\n': #si la ligne n'est pas vite
        
        info = lines[i].strip().split("\t")
        w = re.sub('\s+', 'Espace', info[1])

        outputFile.write( w + "/" + corresDict[info[5]] + " ") #ecriture du mot et du tag correct dans le fichier

    else:
        outputFile.write("\n")  #sinon, aller a la ligne

#fermeture des fichiers
inputFile.close()
outputFile.close()