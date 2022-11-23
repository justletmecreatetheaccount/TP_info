class Duree:
    """
    Classe possédant un attribut hours, minutes et seconds

    -1 < hours < 25 => heures (int)
    -1 < minutes < 61 => minutes (int)
    -1 < seconds < 61 => secondes (int)
    """
    def __init__(self, h, m, s):
        
        if h > 24:
            raise ValueError("H is greater than 24")
        if m >= 60:
            raise ValueError('M is greater than 59')
        if s >= 60:
            raise ValueError('S is greater than 59')
        if h <= -1 or m <= -1 or s <= -1:
            raise ValueError("No negative times allowed")
        if type(h) != int or type(m) != int or type(s) != int:
            raise TypeError("Time encoding must be done with integers")

        self.hours = h
        self.minutes = m
        self.seconds = s
    
    def to_seconds(self):
        return (self.hours * 3600) + (self.minutes * 60) + self.seconds

    def delta(self, d):
        return self.to_seconds() - d.to_seconds()

    def apres(self, d):
        return True if self.delta(d) > 0 else False

    def ajouter(self, d):
        secondes_s = self.to_seconds() + d.to_seconds()
        return Duree(secondes_s // 3599, secondes_s % 3600 // 60, (secondes_s % 3600) % 60)

    def __str__(self):
        return "{:0>2}::{:0>2}::{:0>2}".format(self.hours, self.minutes, self.seconds)

class chanson:
    """
    Classe possédant un attribut titre, artiste et un attribut durée

    title => titre (str)
    artist => artiste (str)
    lenght => durée de la chanson (instance de la classe durée)
    """
    def __init__(self, t, a, d):
        self.title = t
        self.artist = a
        self.lenght = d

    def __str__(self):
        return "{} - {} - {}".format(self.lenght, self.artist, self.title)

class album:
    """
    Classe possédant un attribut numero, une liste d'instances de chanson et un attribut durée

    id => numéro de l'album (int)
    songs => liste de chansons (instances de la classe chanson)
    lenght => somme de la durée de toutes les chansons (une instance de la classe durée)
    """
    def __init__(self, number):
        self.id = number
        self.songs = []
        self.lenght = Duree(0,0,0)

    def add(self, song : chanson):
        """
        Ajoute une instance de chanson à la liste songs de l'album sous certaines conditions

        Ajoute une instance de chanson à la liste 'songs' si sa longueur n'a pas dépassé 100 et si
        la variable 'lenght' sommée de la durée de la chanson ne dépassent pas 1h15

        pre : 
        instance de la classe album
        instance de la classe chanson

        post :
        Si les conditions sont remplies, la liste 'songs' est modifiée de l'instance de la classe 
        chanson qui est ajoutée en bout de liste, la variable lenght est mise à jour et la méthode retourne 'True'
        Si les conditions ne sont pas remplies, la liste 'songs' et la variable lenght ne sont pas modifiées
        et la methode retourne 'False'
        """
        if len(self.songs) == 100:
            return False
        
        if Duree.ajouter(self.lenght, song.lenght).to_seconds() > Duree(1,15,0).to_seconds():
            return False

        self.lenght = Duree.ajouter(self.lenght, song.lenght)
        self.songs.append(song)
        return True

    def __str__(self):

        song : chanson
        list_s = ''
        for song in self.songs:
            list_s += '{:>02} - {} - {} - {}\n'.format(self.songs.index(song) + 1, song.artist, song.title, song.lenght)
            
        return 'Album n°{} - {} chansons - {}\n\n'.format (self.id, len(self.songs), self.lenght) + list_s + "\n"


def read_doc():

    with open('music-db.txt') as file:
        all_songs = []
        repertoire = {}

        for line in file:            
            words = line.split(" ")
            try:
                words[0] = chanson(words[0], words[1], Duree(0, int(words[2]), int(words[3])))
                all_songs.append(words[0])
            except:
                raise ValueError(f"Improper file encoding at line {len(all_songs) + 1}")

        album_number = 0
        for song in all_songs:
            try:
                if repertoire[album_number].add(song) == False:
                    raise ValueError("too many musics creating new album")
            except:
                album_number += 1
                repertoire[album_number] = album(album_number)
                repertoire[album_number].add(song)

        for a in repertoire:
            print(repertoire[a])

read_doc()