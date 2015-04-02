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



def classifie():
    pass
    dicPos = {}
    dicNeg = {}
    tos = {
        True : "pos",
        False : "neg"
    }

    pathPos = "data/tagged/tagged/pos"
    pathNeg = "data/tagged/tagged/neg"

    trains = (
        (pathPos, selectRandom.isTrainPos, dicPos),
        (pathNeg, selectRandom.isTrainNeg, dicNeg)
    )
    for t in trains:
        path = t[0]
        filter = t[1]
        dic = t[2]
        workForFiles(path, filter, lambda file: openFile.traiteFichier(file, dic))


    probaPos = openFile.dictToProba(dicPos)
    probaNeg = openFile.dictToProba(dicNeg)

    def calculSum(dicFile, dicProba):
        res = 1
        for word, count in dicFile.items():
            if word in dicProba:
                res *= math.pow(dicProba[word], count)

        return res
    nb = {
        True:0,
        False:0
    }
    def testFile(file):
        global nbOk
        global nbKo
        dic = {}
        openFile.traiteFichier(file, dic)
        sumPos = calculSum(dic, probaPos) * 100
        sumNeg = calculSum(dic, probaNeg) * 100
        res = tos[sumPos > sumNeg]
        ok =  res in file
        nb[ok] += 1
        print("Result for %s %s : %g%%+ %g%%-" % (file, res, sumPos, sumNeg))

    tests = (
        (pathPos, selectRandom.isTestPos),
        (pathNeg, selectRandom.isTestNeg)
    )
    for t in tests:
        path = t[0]
        filter = t[1]
        workForFiles(path, filter, testFile)


    print("nb", nb)

if __name__ == "__main__":
    classifie()
