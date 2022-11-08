import search

if __name__ == '__main__':
    def index():
        document = request.get("https://inginious.info.ucl.ac.be/course/LSINF1101-PYTHON/REAL07/episodeIV_dialogues.txt")
        print (search.create_index(document))
