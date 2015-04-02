__author__ = 'Jules'

acceptType = ("VER", "NOM", "ADV")
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

def dictToProba(dict):
    nbTot = sum(dict.values())
    div = float(nbTot + len(dict))
    return {key: (value + 1) / div for key, value in dict.items()}



if __name__ == "__main__":
    d1 = {}
    traiteFichier("data/tagged/tagged/neg/neg-0000.txt", d1)
    print(d1)
    print(dictToProba(d1))
    test = {"kill": 4, "bomb":3, "kidnap":6, "music":0, "tv":1, "movie":1}
    print(dictToProba(test))
