from cubeIdx import tierUpList, tierIdx
import random

class TierUpSimulator:
    def __init__(self, cubeName: str, startTier: str, targetTier: str)-> str:
        self.cubeName = cubeName
        self.startTier = startTier
        self.targetTier = targetTier

    def tierUp(self, repetition: int):
        cubeI = 0 if self.cubeName == 'glowing' else 1
        mult = 12000000 if self.cubeName == 'glowing' else 22000000
        probList = tierUpList[cubeI]

        total = 0

        for _ in range(repetition):
          count = 0
          current = tierIdx[self.startTier]
          target = tierIdx[self.targetTier]
          while current != target:
              count += 1
              rng = random.uniform(0, 100)
              if rng <= probList[current]:
                current += 1
          total += count

        avg = round(total / repetition, 2)
        money = round(mult * avg)
        return f"You used on average {avg} {self.cubeName} cubes to tier up from {self.startTier} to {self.targetTier}.\nYou spent {money:,} mesos"
            

    def miracleTierUp(self, repetition: int):
        cubeI = 0 if self.cubeName == 'glowing' else 1
        mult = 12000000 if self.cubeName == 'glowing' else 22000000
        probList = tierUpList[cubeI]

        total = 0

        for _ in range(repetition):
          count = 0
          current = tierIdx[self.startTier]
          target = tierIdx[self.targetTier]
          while current != target:
              count += 1
              rng = random.uniform(0, 100)
              if rng <= probList[current] * 2:
                current += 1
          total += count

        avg = round(total / repetition, 2)
        money = round(mult * avg)
        return f"You used on average {avg} {self.cubeName} cubes to tier up from {self.startTier} to {self.targetTier} during Miracle Time.\nYou spent {money:,} mesos"
            
            



    