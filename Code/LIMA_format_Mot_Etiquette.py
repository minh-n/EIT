#Exo II.3 : analyse morpho-syntaxique
#représenter les étiquettes sous le format "Mot_etiquette"
import numpy as np

inputFile = open("wsj_0010_sample.txt.conll","r")
outputFile = open("mot_etiquette_output.txt","w")

line = inputFile.readlines()

for i in range(len(line)):
	line[i] = line[i].split('\t') #enlever les tabs
	if len(line[i]) >= 4:

		mots = line[i][1].split(' ')

		for mot in mots:
			outputFile.write(mot + "_" + line[i][4] + " ") 