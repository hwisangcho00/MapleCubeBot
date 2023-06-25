import cubeProb
import random
import re
from cubeIdx import equipmentIdx, validCheckList


class CubeSimulator:
    
    def __init__(self, cubeName, tier, equipment, level) -> None:
        self.cubeName = cubeName
        self.tier = tier
        self.equipment = equipment
        self.level = int(level)
        self.validCount = [0] * len(validCheckList)
        

    def rollCube(self) -> str:
        prob = 100
        resLine = None
        for lineNum in range(3):
            print(self.validCount)
            probList = self.getProbList(lineNum)
            if lineNum != 0:
                self.changeProb(prob, probList, resLine)
            resLine = self.rollLine(probList, prob)
            self.updateValidCount(resLine)
            print((lineNum + 1),'Line =',resLine)


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
            return cubeProb.legendary[equipmentIdx[self.equipment]][levelIdx][lineNum].copy()
        
    def changeProb(self, prob, probList, resLine):
        pass

    def updateValidCount(self, resLine):
        
        for idx, potential in enumerate(validCheckList):
            if re.match(potential, resLine):
                self.validCount[idx] += 1
                break
        
        return
        


        