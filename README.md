# EIT
Extraction d'information à partir de textes

***********************************

PTBtoUniv.py : permet de changer les tags PTB d'un fichier en suivant une table de correspondance

Syntax: python PTBtoUniv.py Path_To_POSTags_PTB_Universal_Linux.txt Path_To_Input.txt Path_to_output.txt
Example: python PTBtoUniv.py POSTags_PTB_Universal_Linux.txt wsj_0010_sample.txt.pos.stanford wsj_0010_sample.txt.pos.univ.stanford

***********************************

FormatNER.py : represente un resultat de l'outil de reconnaissance des entites nommees de Stanford sous une nouvelle forme

Syntax: python FormatNER.py Path_To_Input.txt Path_to_output.txt
Example: python FormatNER.py formal-tst.NE.key.04oct95_small.txt.output new-format.NE.key.04oct95_small.txt

***********************************

FormatRefToLima.py : transforme les balises ENAMEX d'un fichier en "\_TAG"

Syntax: python FormatRefToLima.py Path_To_Input.txt Path_to_output.txt
Example: python FormatRefToLima.py formal-tst.NE.key.04oct95_small.ne output.04oct95.ne.lima

***********************************

FormatEspace.py : transforme les "Espaces" compris dans les mots composes comme "BocaEspaceRaton_TAG" en "Boca_TAG Raton_TAG"

Syntax: python FormatEspace.py Path_To_Input.txt Path_to_output.txt
Example: python FormatEspace.py output.04oct95.ne.lima output.04oct95.ne.stanford

***********************************

LimaToStanford.py : permet de changer les tags LIMA d'un fichier en suivant une table de correspondance (identique a PTBtoUniv.py)

Syntax: python LimaToStanford.py Path_To_POSTags_LIMA_Stanford.txt Path_To_Input.txt Path_to_output.txt
Example: 

***********************************

toEvaluateFormat.py : modifie les etiquettes des entites nommes "/TAG" en "\_TAG" pour pouvoir utiliser le script evaluate.py

Syntax: python toEvaluateFormat.py Path_To_Input.txt Path_to_output.txt
Example: python toEvaluateFormat.py formal-tst.NE.key.04oct95_small.txt.output stanford.eval.txt.output
