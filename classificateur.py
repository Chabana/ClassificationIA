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
    if not ok:
        print("Result for %s %s : %g%%+ %g%%-" % (file, res, sumPos, sumNeg))

def classifie():
    pass
    dicPos = {}
    dicNeg = {}


    pathPos = "data/tagged/tagged/pos"
    pathNeg = "data/tagged/tagged/neg"
    #pathPos = "test/pos"
    #pathNeg = "test/neg"
    #selectRandom.isTrainNeg = selectRandom.isTrainPos = lambda file : True
    #selectRandom.isTestNeg = selectRandom.isTestPos = lambda file : True

    workForFiles(pathPos, selectRandom.isTrainPos, lambda file: openFile.traiteFichier(file, dicPos))
    workForFiles(pathNeg, selectRandom.isTrainNeg, lambda file: openFile.traiteFichier(file, dicNeg))

    print("dicPos %s" % repr(dicPos))
    print("dicNeg %s" % repr(dicNeg))

    words = list(dicPos.keys())
    words.extend(x for x in dicNeg.keys() if x not in words)
    words.sort()

    print("words %s" % repr(words))

    print("pos")
    probaPos = openFile.dictToProba(dicPos, words)
    print("neg")
    probaNeg = openFile.dictToProba(dicNeg, words)
    print("probaPos %s" % repr(probaPos))
    print("probaNeg %s" % repr(probaNeg))

    nb = {
        True:0,
        False:0
    }
    #pathNeg = "test"
    workForFiles(pathPos, selectRandom.isTestPos, lambda file: testFile(file, nb, probaPos, probaNeg))
    workForFiles(pathNeg, selectRandom.isTestNeg, lambda file: testFile(file, nb, probaPos, probaNeg))


    print("nb", nb)
    print("rate %f%%" %(100.0 * nb[True] / float(nb[True] + nb[False])))

if __name__ == "__main__":
    classifie()
