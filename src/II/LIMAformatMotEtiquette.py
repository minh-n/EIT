#Exo II.3 : analyse morpho-syntaxique
#representer les etiquettes sous le format "Mot_etiquette"
import numpy as np

inputFile = open(sys.argv[1],"r") #wsj_0010_sample.txt.conll
outputFile = open(sys.argv[2], "w") #mot_etiquette_output.txt

lines = inputFile.readlines()

for i in range(len(lines)):
	lines[i] = lines[i].split('\t') 
	if len(lines[i]) >= 4:

		mots = lines[i][1].split(' ')

		for mot in mots:
			if(mot == "."):
				outputFile.write(mot + "_" + ". ")
			elif (mot == ","):
			 	outputFile.write(mot + "_" + ", ")
			else:
				outputFile.write(mot + "_" + lines[i][4] + " ") 


#fermeture des fichiers
inputFile.close()
outputFile.close()
