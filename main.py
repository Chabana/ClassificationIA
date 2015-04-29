import openFile

import os
import os.path
import math
import time
import enum

def dictToProba(dict, words):
    """
    Transforme le dictionnaire des mots avec leurs occurence en un dictionnaire avec leurs probabilitles
    :param dict: dictionnaire mot : occurrance
    :param words: Liste de tous les mots
    :return: dictionnaire mot : probabilite
    """
    nbTot = sum(dict.values())
    div = float(nbTot + len(words))
    return {key: (valOr0(dict, key) + 1) / div for key in words}

def valOr0(dict, key):
    """
    Retourne la valeur pour la clef ou 0
    :param dict: dictionnaire
    :param key: clef
    :return: dict[key} ou 0
    """
    if key in dict:
        return dict[key]
    return 0

def workForFiles(path, filter, callback):
    """
    Appel le callback pour chaque fichier dans le dossier en appliquant le filtre
    :param path: dossier
    :param filter: filtre
    :param callback: callback
    :return:
    """
    for f in [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and filter(f)]:
        file = os.path.join(path, f)
        callback(file)

def calculSum(dicFile, dicProba):
    """
    Fait la somme balesienne du dictionnaire
    :param dicFile: dictionnaire mot : occurance
    :param dicProba: dictionnaire mot : probabilitl
    :return: probabilite
    """
    res = 1
    for word, count in dicFile.items():
        if word in dicProba:
            res *= math.pow(dicProba[word], count)
    return res

def testFile(file, nb, probaPos, probaNeg, traiteFichier):
    """
    Test un fichier
    :param file: path du fichier
    :param nb: dictionnaire des nombres de fichier ok ou pas
    :param probaPos: dictionnaire des proba positioves
    :param probaNeg: dictionnaire des proba negatives
    :param traiteFichier: fonction pour ouvrir le fichier
    :return:
    """
    tos = {
        True : "pos",
        False : "neg"
    }
    dic = {}
    #traite le fichier
    traiteFichier(file, dic)
    #calcule les somme
    sumPos = calculSum(dic, probaPos)
    sumNeg = calculSum(dic, probaNeg)
    #type dweuit
    res = tos[sumPos > sumNeg]
    #si bon type
    ok = res in file
    if (ok):
        res = Result.Ok
    elif res == "pos":
        res = Result.NegAsPos
    else:
        res = Result.PosAsNeg
    nb[res] += 1

class Mode(enum.Enum):
    """
    Modes d'ouverture des fichiers
    """
    TAGGED = 0,
    NORMAL = 1,
    NORMAL_EXCLUSION = 2,

class Result(enum.Enum):
    #type de resultat
    Ok = 1,
    NegAsPos = 2, #negatif classe positif
    PosAsNeg = 3, #positif classe negatif

def main():
    import fileSelector
    #Nombre de fichier ou de part
    n = 5
    #tableaux
    rates = {mode: {result : 0 for result in Result} for mode in Mode}
    times = {mode: 0 for mode in Mode}
    useBloc = False
    if useBloc:
        fct = fileSelector.createBlockSelectors
    else:
        fct = fileSelector.createRandomSelectors

    for selector in fct(n):
        for mode in Mode:
            rate, time =  classifie(mode, selector)
            for result in Result:
                rates[mode][result] += rate [result]
            times[mode] += time

    for mode in Mode:
        for result in Result:
            rates[mode][result] /= n
        times[mode] /= n
        print("Mean %s : %s in %f seconds" % (mode.name, rates[mode], times[mode]))

#dossier par type
pathPase = {
    Mode.TAGGED : "data/tagged/tagged",
    Mode.NORMAL : "data",
    Mode.NORMAL_EXCLUSION : "data"
}
# fonciton pour traiter les fichier
traiteFichiers = {
    Mode.TAGGED : openFile.traiteFichierTagged,
    Mode.NORMAL : openFile.traiterFicherNormal,
    Mode.NORMAL_EXCLUSION : lambda file, dic: openFile.traiterFicherNormal(file, dic, openFile.loadExclusion())
}

def classifie(mode, fileSelector):
    """
    Classifie les fichier
    :param mode: Types de fichiers
    :param fileSelector: Selecteur de fichier test / exercice
    :return:
    """
    initTime = time.time()
    dicPos = {}
    dicNeg = {}
    #recuperation des dossiers
    pathPos = pathPase[mode] + "/pos"
    pathNeg = pathPase[mode] + "/neg"
    #fonction de traitement
    traiteFichier = traiteFichiers[mode]

    #recupration des occurences pour les fichiers d'entraniement
    workForFiles(pathPos, fileSelector.isTrainPos, lambda file: traiteFichier(file, dicPos))
    workForFiles(pathNeg, fileSelector.isTrainNeg, lambda file: traiteFichier(file, dicNeg))

    #recuperation de la liste de tous les mots
    words = list(dicPos.keys())
    words.extend(x for x in dicNeg.keys() if x not in words)
    words.sort()

    #calcule des probabilitees
    probaPos = dictToProba(dicPos, words)
    probaNeg = dictToProba(dicNeg, words)

    #dicitonnaire des résultats
    nb = {
        result : 0 for result in Result
    }

    #calcule des résultats
    workForFiles(pathPos, fileSelector.isTestPos, lambda file: testFile(file, nb, probaPos, probaNeg, traiteFichier))
    workForFiles(pathNeg, fileSelector.isTestNeg, lambda file: testFile(file, nb, probaPos, probaNeg, traiteFichier))

    #calcule des résultats
    somme = float(sum([n for n in nb.values()]) / 2)
    rates = {result : nb[result] / somme for result in Result}
    rates[Result.Ok] /= 2
    #temps passé
    elapsed = time.time() - initTime
    #resultat
    print("rate %s %f%% in %f seconds (%s) / (%s)" %(mode.name, 100.0 * rates[Result.Ok], elapsed, nb, rates))
    return rates, elapsed

if __name__ == "__main__":
    import sys
    if sys.version_info < (3, 4):
        raise Exception("must use python 3.4 or greater")
    main()
