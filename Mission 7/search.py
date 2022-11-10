"""
Mission 7
========

Groupe: Vlad Doniga - Théo Daron
Local: BARB15

Il n'y a pas grand chose a dire sur ce fichier, normalement il fait ce qu'on lui demande :)

AAH et comme promis, les résultats du concours ! 

Le gagnant est....roulement de tambours...

PAS DISPO SUR LE GITHUB HEHE FALLAIT TROUVER LA CLE

(Pssst, en fait on a quand même fait un script pour chiffrer ce fichier, s'il t'intéresse il est disponible ici: https://github.com/Kaporos/Enigware)

"""

class Indexer:
    def __init__(self) -> None:
        self.index = {}
    def _readfile(self, filename):
        """
        pre : Ouvre le fichier du nom de filename
        post : Retourne une liste avec chaque ligne du fichier
        """
        try :
            with open (filename) as file:
                return file.readlines() 
        except:
            return []  
    def _get_words(self,line):
        """
        pre : prends une ligne (string)
        post : separe la string en mots (ici definis comme ensemble de lettres separes par tout charactere ne faisant pas partie de l'aphabet)
        """
        line = line.lower()
        word = ""
        list = []
        for i in line:
            if i.isalpha():
                word += i
            else:
                if word != "":
                    list.append(word) 
                word = ""
        if word != "": #Dernier mot de la liste
            list.append(word)
        return list

    def create_index(self,filename):
        self.index = {}
        """
        pre : un ficher contenant du texte
        post : retourne un dictionnaire contenant chaque mot du fichier ainsi que leur ligne d'apparition
        """
        for (line_number, line) in enumerate(self._readfile(filename)):
            line_number += 1 #Parce que les numéros de ligne commencent a 1 et pas a 0
            wds = self._get_words(line)
            for j in wds:
                if j in self.index.keys():
                    if not line_number in self.index[j]:
                        self.index[j].append(line_number)
                else:
                    self.index[j] = [line_number]
        return self.index
        
    def get_lines(self,words):
        total = []
        for word in words:
            if word in self.index.keys():
                total += self.index[word] # Ajoute les lignes pour chaque mots
        #Si on cherche deux mots une ligne doit etre presente deux fois
        result = []
        for x in total:
            if total.count(x) == len(words) and not x in result:
                result.append(x)
        return result
