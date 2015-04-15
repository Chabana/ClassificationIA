__author__ = 'Jules'

acceptType = ("VER", "NOM", "ADV", "ADJ") # INT
import codecs
def traiteFichier(path, dict):
    with codecs.open(path, "r", "utf-8") as file:
        for line in file:
            split = line.split("\t")
            if len(split) >= 3:
                type = split[1].split(":")[0]
                if type in acceptType:
                    mot = split[2].replace("\n", "")
                    if mot in dict:
                        dict[mot] += 1
                    else:
                        dict[mot] = 1

def dictToProba(dict, words):
    nbTot = sum(dict.values())
    print("nbTot %d" % nbTot)
    div = float(nbTot + len(words))
    print("div %d" % div)
    return {key: (valOr0(dict, key) + 1) / div for key in words}

def valOr0(dict, key):
    if key in dict:
        return dict[key]
    return 0


if __name__ == "__main__":
    d1 = {}
    traiteFichier("data/tagged/tagged/neg/neg-0000.txt", d1)
    print(d1)
    print(dictToProba(d1))
    test = {"kill": 4, "bomb":3, "kidnap":6, "music":0, "tv":1, "movie":1}
    print(dictToProba(test))
