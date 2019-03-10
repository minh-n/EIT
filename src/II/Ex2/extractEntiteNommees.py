#partie II.3 affichage entitee nommees

import sys
import string

occurences = {}
nbMots = 0
f = open(sys.argv[1])

for line in f:
	for word in line.split():
		entite = word.split("_")
		if entite[0] not in string.punctuation:
			nbMots += 1
			if entite[0] not in occurences.keys():
				occurences[entite[0]] = [1, entite[1]]
			else:
				occurences[entite[0]][0] += 1

for mot, truc in occurences.items():
	print("{:>25}\t\t{:>5}\t\t{:>5}\t\t{:.2f}\t\t".format(mot,truc[1],truc[0],(truc[0]/nbMots)*100))
