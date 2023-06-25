import cubeProb
import random
from cubeIdx import equipmentIdx


class CubeSimulator:
    
    def __init__(self, cubeName, tier, equipment, level) -> None:
        self.cubeName = cubeName
        self.tier = tier
        self.equipment = equipment
        self.level = int(level)

    def rollCube(self) -> str:
        prob = 100
        for lineNum in range(3):        
            probList = self.getProbList(lineNum)
            resLine = self.rollLine(probList, prob)
            self.changeProb(prob, probList)
            print(resLine)


    def rollLine(self, probList, prob) -> str:
        
        res = None

        i = 0 if self.cubeName == 'glowing' else 1

        rng = random.uniform(0, 100)
        res = ""
        sum = 0

        for k, v in probList.items():
            sum += v[i]

        for k, v in probList.items():

            if rng > prob - v[i]:
                res = k
                break
            
            prob -= v[i]

        print(rng, res, sum)
        
        return res

    def getProbList(self, lineNum):

        if 120 <= self.level <= 200:
            levelIdx = 0
        elif self.level == 250:
            levelIdx = 1
        else:
            return

        if self.tier == 'legendary':
            return cubeProb.legendary[equipmentIdx[self.equipment]][levelIdx][lineNum]
        
    def changeProb(self, prob, probList):
        pass