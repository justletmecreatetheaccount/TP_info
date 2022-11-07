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
    for l in readfile(filename):
        wds = get_words(l)
        for j in wds:
            if j in d and readfile(filename).index(l) not in d[j]:
                d[j].append(readfile(filename).index(l))
            else:
                d[j] = [readfile(filename).index(l)]
    return d
    
def get_lines(words, index):
    print (index)
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
