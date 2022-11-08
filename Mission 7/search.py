def readfile (filename):
    """
    pre : ouvre le fichier du nom de 'filename
    post : retourne une liste avec chaque ligne du fichier
    """
    try :
        with open (filename) as file:

            return file.readlines() 
    except:

        return []
    
def get_words(line):
    """
    pre : prends une string
    post : separe la string en mots (ici definis comme ensemble de lettres separes par tout charactere ne fesant pas partie de l'aphabet)
    """
    line = line.lower()
    words = ""
    list = []
    for i in range(len(line)):
        if line[i].isalpha():
            words += line[i]
        else:
            if words != "":
                list.append(words) 
            words = ""
        
    return list

def create_index(filename):
    """
    pre : un ficher contenant du texte
    post : retourne un dictionnaire contenant chaque mot du fichier ainsi que leur ligne d'apparition
    """
    d = {}
    for l in range(len(readfile(filename))):
        wds = get_words(readfile(filename)[l])
        for j in wds:
            if j in d and l not in d[j]:
                d[j].append(l)
            else:
                d[j] = [l]

    return d
    
def get_lines(words, index):
    if words[0] in index:
        comp = index[words[0]]
    else:
        return []
    pres = False
    save = []
    for i in comp:
        for j in words:
            if i in index[j]:
                pres = True
            else:
                pres = False
                break
        if pres: 
            save.append(i)

    return save
