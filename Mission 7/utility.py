"""
Mission 7
========

Groupe: Vlad Doniga - Théo Daron
Local: BARB15

Fichier principal à executer, a priori rien de bien compliqué non plus

"""

import search
class bcolors:
    """
    Colors special chars for terminal
    """
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'

def color(text, bcolor, end=bcolors.ENDC):
    """
    Will return a string with colored text
    """
    return f"{bcolor}{text}{end}"
 
indexer = search.Indexer() 
filename = input (color("Spécifiez le nom de fichier: ", bcolors.BLUE))

index = indexer.create_index(filename)
#print (index)
while True:
  words = input (color("Spécifiez les mots a rechercher, en utilisant des espaces entre les mots: ", bcolors.BLUE))
  if words == "exit":
    break
  lines = indexer.get_lines( words.strip().split(" "))
  if len(lines) > 0:
    print(color("Les mots se retrouvent dans ces lignes:", bcolors.GREEN))
    print(",".join([str(x) for x in lines]))
  else:
    print(color("Aucune correspondance trouvée...", bcolors.RED))