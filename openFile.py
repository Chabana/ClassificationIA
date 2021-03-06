import codecs

acceptType = ("VER", "NOM", "ADV", "ADJ")

def traiteFichierTagged(path, dict):
    """
    Ouvre le fichier tagués
    :param path: path du fichier
    :param dict: dicionnaire résultat
    :return:
    """
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

def traiterFicherNormal(path, dict, exclusion=[]):
    """
    Ouvre un fichier normal
    :param path: path du fichier
    :param dict: dicionnaire résultat
    :param exclusion: liste d'exlusion
    :return:
    """
    with codecs.open(path, "r", "utf-8") as file:
        for line in file:
            line = line.replace("\n", "").replace("\r", "")
            split = line.split(" ")
            for mot in split:
                if not mot in exclusion:
                    if mot in dict:
                        dict[mot] += 1
                    else:
                        dict[mot] = 1

exclusions = None
def loadExclusion():
    """
    Charge la liste des mots a exclure
    :return:
    """
    global exclusions
    if exclusions is None:
        exclusions = []
        with codecs.open("data/frenchST.txt", "r", "utf-8") as file:
            for line in file:
                exclusions.append(line.replace("\n", "").replace("\r", ""))
        exclusions = tuple(exclusions)
    return exclusions
loadExclusion()
