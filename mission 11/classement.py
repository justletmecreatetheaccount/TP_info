from ordered_linked_list import *

class Classement(OrderLinkedList):
    """
    Une implémentation primitive de classement, non ordonnée et de capacité fixe.
    @author Kim Mens
    @version 01 Décembre 2019
    """

    def __init__(self, results):
        """
        @pre: -
        @post: un classement vide de taille 0 a été créé
        """
        super.__init__(results)
        self.__size = self.__length

    def size(self):
        """
        Méthode accesseur.
        Retourne la taille de ce classement.
        @pre:  -
        @post: Le nombre de résultats actuellement stockés dans ce classement a été retourné.
        """
        return self.__size

    def get(self,c):
        """
        Retourne le résultat d'un coureur donné.
        @pre c est un Coureur
        @post retourne le premier (meilleur) Resultat r du coureur c dans le
              classement. Retourne None si le coureur ne figure pas (encore)
              dans le classement.
        """
        temps = 0
        result = None
        node = self.__head
        for i in range(self.__length):
            if node.value().coureur() == c and node.value().temps() > temps:
                result = node.value()
                temps = node.value().temps()
        return result

    def get_position(self,c):
        """
        Retourne la meilleure position d'un coureur dans ce classement.
        @pre c est un Coureur
        @post retourne un entier représentant la position du coureur c dans ce classement,
              à partir de 1 pour la tête de ce classement. Si le coureur figure plusieurs fois
              dans le classement, la première (meilleure) position est retournée.
              Retourne -1 si le coureur ne figure pas dans le classement.
        ATTENTION : L'implémentation actuelle ne respecte pas encore la post-condition!
                    Etant donné que la dictionnaire de résultats ne connaît pas de position,
                    pour le moment cette méthode retourne toujours "***position inconnue***".
                    A vous de la corriger en utilisant une liste chaînée ordonnée
                    comme structure de données, plutôt qu'une simple dictionnaire.
        """
        node = self.__head
        for i in range(self.__length):
            if node.value().coureur() == c:
                return i + 1

    def remove(self,c):
        """
        Retire un résultat du classement.
        @pre  c est un Coureur
        @post retire le premier (meilleur) résultat pour le coureur c du classement.
              c est comparé au sens de __eq__. Retourne c si un résultat a été retiré,
              of False si c n'est pas trouvé dans la liste.
        """

        node = self.__head
        if self.__head.value().coureur() == c:
            self.__size -= 1
            self.__head = self.__head.next()
            return c

        for i in range(self.__length):
            if node.next().value().coureur() == c:
                self.__size -= 1
                node.set_next(node.next().next())
                return c
        return False



    def __str__(self):
        """
        Méthode magique
        Retourne une représentation string de cet objet.
        @pre:  -
        @post: Retourne une représentation de ce classement sous forme d'un string,
               avec une ligne par résultat.
        """
        s = ""
        node = self.__head
        for c in range(self.__length):
            s += "  " + str(self.get_position(c)) + " > " + str(node) + "\n"
            node = node.next()

        return s