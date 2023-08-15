import cubeProb
import random
import re
from cubeIdx import equipmentIdx, validCheckList


class CubeSimulator:
    """
    Class that simulates the cubing logic of Maplestory
    """
    def __init__(self, cubeName, equipment, level) -> None:
        self.cubeName = cubeName
        self.cubeI = 0 if self.cubeName == 'glowing' else 1
        self.rank = 'legendary'
        self.equipment = equipment
        self.level = int(level)
        self.validCount = [0] * len(validCheckList)
        

    def rollCube(self) -> str:
        """
        Central method that generates 3 lines of potentials according to Maplestory game logic.
        """
        prob = 100
        resLine = None
        res = ""
        # loop 3 times for each line
        for lineNum in range(3):
            # get the copy of the probability list
            probList = self.getProbList(lineNum)
            # skip the first line
            if lineNum != 0:
                # delete the lines that cannot appear again
                prob = self.changeProb(prob, probList)
            resLine = self.rollLine(probList, prob)
            res += "- " + resLine + "\n"
            print((lineNum + 1), resLine, '\n', self.validCount, '\n', probList, '\n')
            # some potentials cannot appear more than once or twice
            self.updateValidCount(resLine)
        return res

    def rollLine(self, probList, prob) -> str:
        """
        Returns a single potential line given the base probability and probability list
        """
        res = None

        rng = random.uniform(0, 100)
        res = ""

        lastKey = list(probList.keys())[-1]

        for k, v in probList.items():

            if rng > prob - v[self.cubeI]:
                res = k
                break
            
            prob -= v[self.cubeI]
        
        # account for small difference made by rounding up
        if res == "":
            res = lastKey

        return res

    def getProbList(self, lineNum):
        """
        Returns the copy of the corresponding probability list
        """
        if 120 <= self.level <= 150:
            levelIdx = 0
        elif self.level > 150:
            levelIdx = 1
        else:
            return

        if self.rank == 'legendary':
            return cubeProb.legendary[equipmentIdx[self.equipment]][levelIdx][lineNum].copy()
        
    def changeProb(self, prob, probList):
        """
        Given the base probability and copy of the probability list,
        modify them so that potentials that cannot appear more than once or twice are checked
        """
        limit = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
        for idx, potential in enumerate(validCheckList):
            if self.validCount[idx] >= limit[idx]:
                for k, v in list(probList.items()):
                    if re.match(potential, k):
                        # change the base probability
                        prob -= v[self.cubeI]
                        print("The following ability cannot appear anymore : ", k)
                        # delete the potential from the probability list
                        del probList[k]

        return prob

    
    def updateValidCount(self, resLine):
        """
        Using regex to match certain potentials that cannot appear more than once or twice
        """
        for idx, potential in enumerate(validCheckList):
            if re.match(potential, resLine):
                self.validCount[idx] += 1
                break
        
        return
        


        