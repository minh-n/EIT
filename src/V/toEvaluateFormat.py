#partie V

import sys

inputFile = open(sys.argv[1], "r")
outputFile = open(sys.argv[2], "w")

lines = inputFile.readlines()

for i in range(len(lines)):

    for mot in lines[i].split(' '):

        if mot.split("/")[1] == "O": #cas du /O : on enleve le tag
            outputFile.write(mot.replace("/O",""))

        else:   #cas des autres tags (ORGANIZATION...) : on remplace le / par un _
            outputFile.write(mot.replace("/", "_"))
        outputFile.write(" ")
    outputFile.write("\n")