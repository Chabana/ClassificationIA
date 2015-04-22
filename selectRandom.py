import random

nbFiles = 1000
prop = 0.2

class SelectFile:
    def __init__(self, tabPos, tabNeg):
        self.__tabPos = tabPos
        self.__tabNeg = tabNeg
    def isTestPos(self, name):
            return self.isInTab(name, self.__tabPos)
    def isTestNeg(self, name):
        return self.isInTab(name, self.__tabNeg)
    def isTrainPos(self, name):
        return not self.isInTab(name, self.__tabPos)
    def isTrainNeg(self, name):
        return not self.isInTab(name, self.__tabNeg)
    def isInTab(self, name, tab):
        return len([f for f in tab if name.endswith(f)]) > 0

class SelectFileRandom(SelectFile):
    def __init__(self):
        super().__init__(createRandom(nbFiles, prop), createRandom(nbFiles, prop))


def numToText(n):
    s = str(n) + ".txt"
    while len(s) < 8:
        s = "0" + s
    return "-" + s

def createRandom(nb, prop):
    toSelect = int(nb * prop)

    selected=[]
    noSelected=list(range(1000))

    for i in range(toSelect):
        s = noSelected[random.randrange(len(noSelected))]
        selected.append(s)
        noSelected.remove(s)
    selected.sort()
    return list([numToText(n) for n in selected])

TabNeg = ('-0004.txt', '-0012.txt', '-0015.txt', '-0018.txt', '-0024.txt', '-0032.txt', '-0040.txt', '-0044.txt', '-0054.txt', '-0056.txt', '-0069.txt', '-0072.txt', '-0074.txt', '-0078.txt', '-0083.txt', '-0085.txt', '-0092.txt', '-0095.txt', '-0098.txt', '-0100.txt', '-0114.txt', '-0116.txt', '-0125.txt', '-0132.txt', '-0136.txt', '-0147.txt', '-0149.txt', '-0152.txt', '-0156.txt', '-0158.txt', '-0162.txt', '-0166.txt', '-0172.txt', '-0175.txt', '-0181.txt', '-0186.txt', '-0198.txt', '-0206.txt', '-0208.txt', '-0209.txt', '-0216.txt', '-0223.txt', '-0225.txt', '-0241.txt', '-0251.txt', '-0262.txt', '-0272.txt', '-0273.txt', '-0278.txt', '-0302.txt', '-0308.txt', '-0309.txt', '-0310.txt', '-0325.txt', '-0327.txt', '-0330.txt', '-0342.txt', '-0345.txt', '-0353.txt', '-0354.txt', '-0358.txt', '-0367.txt', '-0368.txt', '-0377.txt', '-0378.txt', '-0386.txt', '-0390.txt', '-0395.txt', '-0396.txt', '-0399.txt', '-0406.txt', '-0410.txt', '-0413.txt', '-0417.txt', '-0418.txt', '-0420.txt', '-0422.txt', '-0426.txt', '-0433.txt', '-0440.txt', '-0448.txt', '-0455.txt', '-0457.txt', '-0458.txt', '-0466.txt', '-0467.txt', '-0472.txt', '-0493.txt', '-0496.txt', '-0509.txt', '-0512.txt', '-0513.txt', '-0515.txt', '-0518.txt', '-0519.txt', '-0523.txt', '-0526.txt', '-0529.txt', '-0530.txt', '-0531.txt', '-0538.txt', '-0546.txt', '-0547.txt', '-0548.txt', '-0551.txt', '-0553.txt', '-0555.txt', '-0557.txt', '-0574.txt', '-0580.txt', '-0583.txt', '-0587.txt', '-0597.txt', '-0598.txt', '-0604.txt', '-0607.txt', '-0610.txt', '-0613.txt', '-0621.txt', '-0625.txt', '-0627.txt', '-0628.txt', '-0631.txt', '-0645.txt', '-0655.txt', '-0660.txt', '-0666.txt', '-0673.txt', '-0674.txt', '-0676.txt', '-0684.txt', '-0690.txt', '-0696.txt', '-0702.txt', '-0715.txt', '-0718.txt', '-0721.txt', '-0724.txt', '-0726.txt', '-0732.txt', '-0735.txt', '-0736.txt', '-0739.txt', '-0740.txt', '-0749.txt', '-0751.txt', '-0754.txt', '-0764.txt', '-0766.txt', '-0770.txt', '-0774.txt', '-0776.txt', '-0782.txt', '-0784.txt', '-0785.txt', '-0788.txt', '-0796.txt', '-0798.txt', '-0808.txt', '-0809.txt', '-0811.txt', '-0814.txt', '-0820.txt', '-0834.txt', '-0838.txt', '-0840.txt', '-0849.txt', '-0856.txt', '-0857.txt', '-0862.txt', '-0865.txt', '-0874.txt', '-0883.txt', '-0893.txt', '-0895.txt', '-0899.txt', '-0902.txt', '-0903.txt', '-0906.txt', '-0909.txt', '-0915.txt', '-0923.txt', '-0930.txt', '-0940.txt', '-0951.txt', '-0952.txt', '-0957.txt', '-0960.txt', '-0962.txt', '-0965.txt', '-0966.txt', '-0968.txt', '-0971.txt', '-0973.txt', '-0974.txt', '-0979.txt', '-0984.txt', '-0986.txt', '-0994.txt', '-0996.txt')
TabPos = ('-0007.txt', '-0020.txt', '-0024.txt', '-0039.txt', '-0040.txt', '-0041.txt', '-0046.txt', '-0060.txt', '-0068.txt', '-0074.txt', '-0075.txt', '-0078.txt', '-0081.txt', '-0084.txt', '-0086.txt', '-0088.txt', '-0089.txt', '-0107.txt', '-0108.txt', '-0109.txt', '-0110.txt', '-0115.txt', '-0118.txt', '-0119.txt', '-0121.txt', '-0128.txt', '-0134.txt', '-0135.txt', '-0136.txt', '-0142.txt', '-0144.txt', '-0148.txt', '-0152.txt', '-0155.txt', '-0157.txt', '-0168.txt', '-0170.txt', '-0182.txt', '-0188.txt', '-0195.txt', '-0200.txt', '-0205.txt', '-0209.txt', '-0213.txt', '-0230.txt', '-0236.txt', '-0243.txt', '-0246.txt', '-0248.txt', '-0257.txt', '-0259.txt', '-0260.txt', '-0271.txt', '-0282.txt', '-0284.txt', '-0287.txt', '-0298.txt', '-0302.txt', '-0303.txt', '-0305.txt', '-0309.txt', '-0316.txt', '-0319.txt', '-0328.txt', '-0335.txt', '-0336.txt', '-0341.txt', '-0342.txt', '-0350.txt', '-0365.txt', '-0369.txt', '-0370.txt', '-0372.txt', '-0377.txt', '-0381.txt', '-0383.txt', '-0384.txt', '-0391.txt', '-0393.txt', '-0394.txt', '-0396.txt', '-0414.txt', '-0416.txt', '-0428.txt', '-0438.txt', '-0443.txt', '-0451.txt', '-0452.txt', '-0458.txt', '-0460.txt', '-0465.txt', '-0474.txt', '-0477.txt', '-0482.txt', '-0483.txt', '-0484.txt', '-0490.txt', '-0493.txt', '-0500.txt', '-0502.txt', '-0504.txt', '-0519.txt', '-0521.txt', '-0534.txt', '-0548.txt', '-0549.txt', '-0553.txt', '-0556.txt', '-0558.txt', '-0563.txt', '-0565.txt', '-0568.txt', '-0569.txt', '-0570.txt', '-0572.txt', '-0575.txt', '-0579.txt', '-0581.txt', '-0583.txt', '-0586.txt', '-0597.txt', '-0615.txt', '-0633.txt', '-0635.txt', '-0638.txt', '-0644.txt', '-0650.txt', '-0656.txt', '-0669.txt', '-0670.txt', '-0672.txt', '-0673.txt', '-0678.txt', '-0692.txt', '-0697.txt', '-0702.txt', '-0708.txt', '-0716.txt', '-0720.txt', '-0731.txt', '-0732.txt', '-0736.txt', '-0740.txt', '-0747.txt', '-0751.txt', '-0755.txt', '-0759.txt', '-0761.txt', '-0764.txt', '-0768.txt', '-0778.txt', '-0780.txt', '-0787.txt', '-0789.txt', '-0793.txt', '-0798.txt', '-0811.txt', '-0812.txt', '-0817.txt', '-0827.txt', '-0828.txt', '-0833.txt', '-0835.txt', '-0840.txt', '-0847.txt', '-0849.txt', '-0857.txt', '-0868.txt', '-0882.txt', '-0883.txt', '-0885.txt', '-0888.txt', '-0890.txt', '-0894.txt', '-0897.txt', '-0901.txt', '-0903.txt', '-0904.txt', '-0908.txt', '-0910.txt', '-0922.txt', '-0924.txt', '-0925.txt', '-0928.txt', '-0929.txt', '-0930.txt', '-0931.txt', '-0935.txt', '-0938.txt', '-0941.txt', '-0942.txt', '-0950.txt', '-0958.txt', '-0963.txt', '-0970.txt', '-0974.txt', '-0977.txt', '-0985.txt', '-0986.txt', '-0988.txt')


class SelectFileDeterminist(SelectFile):
    def __init__(self):
        super().__init__(TabPos, TabNeg)

if __name__ == "__main__":
    print(createRandom(nbFiles, prop))
    print(createRandom(nbFiles, prop))
