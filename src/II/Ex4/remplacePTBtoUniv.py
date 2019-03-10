#Exo II.4 : Evaluation de l'analyse morpho-syntaxique
import sys

dicFileTemp = open(sys.argv[1], "r")
dicFileLines = dicFileTemp.readlines()

inputFile = open(sys.argv[2],"r")
outputFile = open(sys.argv[3], "w")

line = inputFile.readlines()


'''
Le tableau de conversion PTB -> universel est de la forme : 
CC CONJ
CD NUM
DT DET
...

On va donc creer un dictionnaire ayant pour clef la 1e colonne
et pour valeur la 2e

'''
dictionnaire = { } 

#remplissage du dictionnaire
for i in range(len(dicFileLines)):
	dicFileLines[i] = dicFileLines[i].split(' ')

	dictionnaire[dicFileLines[i][0]] = dicFileLines[i][1].rstrip()


#remplacement des symboles de Lima par ceux du dictionnaire
for i in range(0, len(line)):
	currentSymbolToReplace = line[i].split(' ')[1].replace('\t', '').replace('\n', '')
	if currentSymbolToReplace in dictionnaire.keys():
		line[i] = str.replace(line[i], currentSymbolToReplace, dictionnaire[currentSymbolToReplace])
	
	#ecriture de la ligne corrigee dans le fichier
	outputFile.write(line[i] + "\n")

#fermeture des fichiers
inputFile.close()
outputFile.close()


