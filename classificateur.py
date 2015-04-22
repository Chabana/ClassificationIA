__author__ = 'Jules'
import openFile

import os
import os.path
import math
import time

def dictToProba(dict, words):
    nbTot = sum(dict.values())
    div = float(nbTot + len(words))
    return {key: (valOr0(dict, key) + 1) / div for key in words}

def valOr0(dict, key):
    if key in dict:
        return dict[key]
    return 0

def workForFiles(path, filter, callback):
    for f in [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and filter(f)]:
        file = os.path.join(path, f)
        callback(file)

def calculSum(dicFile, dicProba):
    res = 1
    for word, count in dicFile.items():
        if word in dicProba:
            res *= math.pow(dicProba[word], count)
    return res

def testFile(file, nb, probaPos, probaNeg, traiteFichier):
    tos = {
        True : "pos",
        False : "neg"
    }
    dic = {}
    traiteFichier(file, dic)
    sumPos = calculSum(dic, probaPos) * 100
    sumNeg = calculSum(dic, probaNeg) * 100
    res = tos[sumPos > sumNeg]
    ok = res in file
    nb[ok] += 1

import enum
class Mode(enum.Enum):
    TAGGED = 0,
    NORMAL = 1,
    NORMAL_EXCLUSION = 2,

def main():
    import selectRandom
    n = 5
    rates = {mode: 0 for mode in Mode}
    times = {mode: 0 for mode in Mode}
    for i in range(5):
        selector = selectRandom.SelectFileRandom()
        for mode in Mode:
            rate, time =  classifie(mode, selector)
            rates[mode] += rate
            times[mode] += time

    for mode in Mode:
        rates[mode] /= n
        times[mode] /= n
        print("Mean %s : %f%% in %f seconds" % (mode.name, 100*rates[mode], times[mode]))


pathPase = {
    Mode.TAGGED : "data/tagged/tagged",
    Mode.NORMAL : "data",
    Mode.NORMAL_EXCLUSION : "data"
}

traiteFichiers = {
    Mode.TAGGED : openFile.traiteFichierTagged,
    Mode.NORMAL : openFile.traiterFicherNormal,
    Mode.NORMAL_EXCLUSION : lambda file, dic: openFile.traiterFicherNormal(file, dic, openFile.loadExclusion())
}

def classifie(mode, selectRandom):
    initTime = time.time()
    dicPos = {}
    dicNeg = {}

    pathPos = pathPase[mode] + "/pos"
    pathNeg = pathPase[mode] + "/neg"

    traiteFichier = traiteFichiers[mode]

    workForFiles(pathPos, selectRandom.isTrainPos, lambda file: traiteFichier(file, dicPos))
    workForFiles(pathNeg, selectRandom.isTrainNeg, lambda file: traiteFichier(file, dicNeg))

    words = list(dicPos.keys())
    words.extend(x for x in dicNeg.keys() if x not in words)
    words.sort()

    probaPos = dictToProba(dicPos, words)
    probaNeg = dictToProba(dicNeg, words)

    nb = {
        True:0,
        False:0
    }

    workForFiles(pathPos, selectRandom.isTestPos, lambda file: testFile(file, nb, probaPos, probaNeg, traiteFichier))
    workForFiles(pathNeg, selectRandom.isTestNeg, lambda file: testFile(file, nb, probaPos, probaNeg, traiteFichier))

    rate = nb[True] / float(nb[True] + nb[False])
    elapsed = time.time() - initTime
    print("rate %s %f%% in %f seconds" %(mode.name, 100.0 * rate, elapsed))
    return rate, elapsed

if __name__ == "__main__":
    main()
