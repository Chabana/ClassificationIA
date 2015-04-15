__author__ = 'Jules'
import openFile
import selectRandom
import os
import os.path
import math

def workForFiles(path, filter, callback):
    for f in [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and filter(f)]:
        file =  os.path.join(path, f)
        callback(file)

def calculSum(dicFile, dicProba):
    res = 1
    for word, count in dicFile.items():
        if word in dicProba:
            res *= math.pow(dicProba[word], count)
    return res
def testFile(file, nb, probaPos, probaNeg):
    tos = {
        True : "pos",
        False : "neg"
    }
    dic = {}
    openFile.traiteFichier(file, dic)
    sumPos = calculSum(dic, probaPos) * 100
    sumNeg = calculSum(dic, probaNeg) * 100
    res = tos[sumPos > sumNeg]
    ok = res in file
    nb[ok] += 1
    print("Result for %s %s : %g%%+ %g%%-" % (file, res, sumPos, sumNeg))

def classifie():
    pass
    dicPos = {}
    dicNeg = {}


    pathPos = "data/tagged/tagged/pos"
    pathNeg = "data/tagged/tagged/neg"

    workForFiles(pathPos, selectRandom.isTrainPos, lambda file: openFile.traiteFichier(file, dicPos))
    workForFiles(pathNeg, selectRandom.isTrainNeg, lambda file: openFile.traiteFichier(file, dicNeg))

    probaPos = openFile.dictToProba(dicPos)
    probaNeg = openFile.dictToProba(dicNeg)

    nb = {
        True:0,
        False:0
    }

    workForFiles(pathPos, selectRandom.isTestPos, lambda file: testFile(file, nb, probaPos, probaNeg))
    workForFiles(pathNeg, selectRandom.isTestNeg, lambda file: testFile(file, nb, probaPos, probaNeg))


    print("nb", nb)
    print("rate %f%%" %(100.0 * nb[True] / float(nb[True] + nb[False])))

if __name__ == "__main__":
    classifie()
