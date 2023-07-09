import cubeProb
import random
import re
from cubeIdx import equipmentIdx, validCheckList


class CubeSimulator:
    
    def __init__(self, cubeName, rank, equipment, level) -> None:
        self.cubeName = cubeName
        self.cubeI = 0 if self.cubeName == 'glowing' else 1
        self.rank = rank
        self.equipment = equipment
        self.level = int(level)
        self.validCount = [0] * len(validCheckList)
        

    def rollCube(self) -> str:
        prob = 100
        resLine = None
        res = ""
        for lineNum in range(3):
            probList = self.getProbList(lineNum)
            if lineNum != 0:
                prob = self.changeProb(prob, probList)
            resLine = self.rollLine(probList, prob)
            res += resLine + "\n"
            print((lineNum + 1), resLine, '\n', self.validCount, '\n', probList, '\n')
            self.updateValidCount(resLine)
        return res

    def rollLine(self, probList, prob) -> str:
        
        res = None

        rng = random.uniform(0, 100)
        res = ""
        sum = 0

        lastKey = list(probList.keys())[-1]

        for k, v in probList.items():
            sum += v[self.cubeI]

        for k, v in probList.items():

            if rng > prob - v[self.cubeI]:
                res = k
                break
            
            prob -= v[self.cubeI]
        
        if res == "":
            res = lastKey

        return res

    def getProbList(self, lineNum):

        if 120 <= self.level <= 150:
            levelIdx = 0
        elif self.level > 150:
            levelIdx = 1
        else:
            return

        if self.rank == 'legendary':
            return cubeProb.legendary[equipmentIdx[self.equipment]][levelIdx][lineNum].copy()
        
    def changeProb(self, prob, probList):
        i = 0 if self.cubeName == 'glowing' else 1
        limit = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        for idx, potential in enumerate(validCheckList):
            if self.validCount[idx] >= limit[idx]:
                for k, v in list(probList.items()):
                    if re.match(potential, k):
                        prob -= v[self.cubeI]
                        print("The following ability cannot appear anymore : ", k)
                        del probList[k]

        return prob

    
    def updateValidCount(self, resLine):
        
        for idx, potential in enumerate(validCheckList):
            if re.match(potential, resLine):
                self.validCount[idx] += 1
                break
        
        return
        


        