"""
Vlad Doniga
"""

###############
### ARTICLE ###
###############

"""
Cette classe représente un Article de facture simple,
comprenant un descriptif et un prix.
   
@author Kim Mens
@version 4 novembre 2021
"""
class Article :

    def __init__(self,d,p):
        """
        @pre:  d un string décrivant l'article
               p un float représentant le prix HTVA en EURO d'un exemplaire de cet article 
        @post: Un article avec description d et prix p a été créé.
        Exemple: Article("carte graphique", 119.49)
        """
        self.__description = d
        self.__prix = p
        
    def description(self) :
        """
        @post: retourne la description textuelle décrivant l'article.
        """
        return self.__description

    def prix(self) :
        """
        @post: retourne le prix d'un exemplaire de cet article, hors TVA.
        """
        return self.__prix
        
    def taux_tva(self):
        """
        @post: retourne le taux de TVA (même valeur pour chaque article)
        """    
        return 0.21   # TVA a 21%

    def tva(self):
        """
        @post: retourne la TVA sur cet article
        """    
        return self.prix() * self.taux_tva()
 
    def prix_tvac(self):
        """
        @post: retourne le prix d'un exemplaire de cet article, TVA compris.
        """
        return self.prix() + self.tva()

    def __str__(self):
        """
        @post: retourne un string decrivant cet article, au format: "{description}: {prix}"
        """
        return "{0}: {1:.2f} EUR".format(self.description(), self.prix())

###############
### FACTURE ###
###############

"""
Cette classe représente une Facture, sous forme d'une liste d'articles.
   
@author Kim Mens
@version 4 novembre 2021
"""

class Facture :
    numero_pro_facture = 1

    def __init__(self, d, a_list):
        """
        @pre  d est un string court décrivant la facture;
              a_list est une liste d'objets de type Article.
        @post Une facture avec une description d et un liste d'articles a_list été crée.
        Exemple: Facture("PC Store - 22 novembre", [ Article("carte graphique", 119.49) ])
        """
        self.__description = d
        self.__articles = a_list
        self.numero_facture = Facture.numero_pro_facture
        Facture.numero_pro_facture += 1
        
    def description(self) :
        """
        @post: retourne la description de cette facture.
        """
        return self.__description
    
    def __str__(self):
        """
        @post: retourne la représentation string d'une facture, à imprimer avec la méthode print().
        (Consultez l'énoncé pour un exemple de la représentation string attendue.)
        """
        s = self.entete_str()
        totalPrix = 0.0
        totalTVA = 0.0
        for art in self.__articles :
            s += self.article_str(art)
            totalPrix = totalPrix + art.prix()
            totalTVA = totalTVA + art.tva()
        s += self.totaux_str(totalPrix, totalTVA)
        return s

    def entete_str(self):
        """
        @post: retourne une représentation string de l'entête de la facture, comprenant le descriptif
               et les entêtes des colonnes.
        """
        return "Facture No {} ".format(self.numero_facture) + self.__description + "\n" \
               + self.barre_str() \
               + "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","prix HTVA","TVA","prix TVAC") \
               + self.barre_str()

    def barre_str(self):
        """
        @post: retourne un string représentant une barre horizontale sur la largeur de la facture
        """
        barre_longeur = 83
        return "="*barre_longeur + "\n"

    def article_str(self, art):
        """
        @pre:  art une instance de la classe Article
        @post: retourne un string correspondant à une ligne de facture pour l'article art
        """
        return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.description(), art.prix(), art.tva(), art.prix_tvac())

    def totaux_str(self, prix, tva):
        """
        @pre:  prix un float représentant le prix total de la facture en EURO
               tva un float représentant le TVA total de la facture en EURO
        @post: retourne un string représentant une ligne de facture avec les totaux prix et tva,
               à imprimer en bas de la facture
        """
        return self.barre_str() \
               + "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format("T O T A L", prix, tva, prix + tva) \
               + self.barre_str()
        
    # Cette méthode doit être ajouté lors de l'étape 2.5 de la mission    
    def nombre(self, pce) :
        """
        @pre:  pce une instance de la classe Piece
        @post: retourne le nombre d'articles de type ArticlePiece dans la facture,
               faisant référence à une pièce qui est égale à pce,
               en totalisant sur tous les articles qui contiennent une telle pièce.
        """
        number = 0
        for object in self.__articles:
            if type(object) == ArticlePiece:
                if object.piece() == pce:
                    number += object.number()
            else:
                number += 1
        return number

    def entete_str_l(self):
        """
        @post: retourne une représentation string de l'entête de la facture, comprenant le descriptif
               et les entêtes des colonnes.
        """
        return "Livraison - Facture No {} : ".format(self.numero_facture) + self.__description + "\n" \
               + self.barre_str() \
               + "| {0:<40} | {1:>10} | {2:>10} | {3:>10} |\n".format("Description","poids/pce","nombre","poids") \
               + self.barre_str()

    def article_str_l(self, art):
        """
        @pre:  art une instance de la classe Article
        @post: retourne un string correspondant à une ligne de facture pour l'article art
        """
        if not art.piece().fragile():
            return "| {0:40} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.piece().description(), art.piece().poids(), art.number(), art.piece().poids() * art.number())
        else:
            return "| {0:36} | {1:10.2f} | {2:10.2f} | {3:10.2f} |\n".format(art.piece().description() + " (!)", art.piece().poids(), art.number(), art.piece().poids() * art.number())

    def totaux_str_l(self, nombre, nombre_tot, poids_tot):
        """
        @pre:  prix un float représentant le prix total de la facture en EURO
               tva un float représentant le TVA total de la facture en EURO
        @post: retourne un string représentant une ligne de facture avec les totaux prix et tva,
               à imprimer en bas de la facture
        """
        return self.barre_str() \
            + "| {0:40} |            | {1:10.2f} | {2:10.2f} |\n".format(str(nombre) + " articles", nombre_tot, poids_tot) \
            + self.barre_str()

    def print_livraison(self):

        # Cette méthode doit être ajouté lors de l'étape 2.6 de la mission
        s = "Livraison - " + self.entete_str_l()
        totalNombre = 0
        totalPoids = 0.00
        articles = 0
        for art in self.__articles :
            if type(art) == ArticlePiece :
                s += self.article_str_l(art)
                articles += 1
                totalNombre += (art.number())
                totalPoids += art.piece().poids()*art.number()
        s += self.totaux_str_l(articles, totalNombre, totalPoids)
        for art in self.__articles :
            if type(art) == ArticlePiece :
                if art.piece().fragile() == True:
                    s += "(!) *** livraison fragile ***"
                    break
        print(s)
    def livraison_str(self):
        """
        Cette méthode est une méthode auxiliaire pour la méthode printLivraison
        """
        pass

class ArticleReparation(Article):
    def __init__(self, d, duration = 0, prix_fixe = 20, prix_variable = 35):
        super().__init__(d, prix_fixe + prix_variable * duration)
        if type(duration) != float and type(duration) != int:
            raise TypeError("Time must be recorded as a number")
        self.__duration = duration

    def description(self):
        return super().description() + ' ({} heures)'.format(self.__duration)

class Piece():
    def __init__(self, d, p, wh = 0, fra = False, rtva = False):
        self.__description = d
        self.__prix = p
        self.__weight = wh
        self.__fragile = fra
        self.__reducedtva = rtva

    def description(self):
        return self.__description
    def prix(self):
        return self.__prix
    def poids(self):
        return self.__weight

    def fragile(self):
        return self.__fragile
    def tva_reduit(self):
        return self.__reducedtva
    def __eq__(self, o):
        return type(self) == type(o) and self.__description == o.description() and self.__prix == o.prix() # and self.__weight == o.poids() and self.__fragile == o.fragile() and self.__reducedtva == o.tva_reduit()

class ArticlePiece(Article):
    def __init__(self, number, piece):
        self.__number = number
        self.__piece : Piece = piece

    def number(self):
        return self.__number
    def piece(self):
        return self.__piece

    def description(self):
        return "{} * {} @ {}".format(self.__number, self.__piece.description(), self.__piece.prix())
    def prix(self):
        return self.__piece.prix() * self.__number
    def taux_tva(self):
        return 0.06 if self.__piece.tva_reduit() else 0.21

#########################
### ARTICLEREPARATION ###
#########################

# Cette classe doit être ajouté lors de l'étape 2.2 de la mission    

#############
### PIECE ###
#############

# Cette classe doit être ajouté lors de l'étape 2.3 de la mission    

####################
### ARTICLEPIECE ###
####################

# Cette classe doit être ajouté lors de l'étape 2.3 de la mission    

########################
### RUNNING THE CODE ###
########################

# Ajouter votre code ici pour imprimer une facture et un borderaux
# de livraison.