def readfile (filename):
    try :
        with open (filename) as file:
            list = file.readlines()
            return list
    except:
        return []
    
def get_words(line):
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
    d = {}
    for i in readfile(filename):
        d[get_words(i)] = 