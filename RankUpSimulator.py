from cubeIdx import rankUpList, rankIdx
import random

class RankUpSimulator:
    def __init__(self, cubeName: str, startRank: str, targetRank: str)-> str:
        self.cubeName = cubeName
        self.startRank = startRank
        self.targetRank = targetRank

    def rank(self, repetition: int):
        cubeI = 0 if self.cubeName == 'glowing' else 1
        mult = 12000000 if self.cubeName == 'glowing' else 22000000
        probList = rankUpList[cubeI]

        total = 0

        for _ in range(repetition):
          count = 0
          current = rankIdx[self.startRank]
          target = rankIdx[self.targetRank]
          while current != target:
              count += 1
              rng = random.uniform(0, 100)
              if rng <= probList[current]:
                current += 1
          total += count

        avg = round(total / repetition, 2)
        money = round(mult * avg)
        return f"You used on average {avg} {self.cubeName} cubes to rank up from {self.startRank} to {self.targetRank}.\nYou spent {money:,} mesos"
            
            

    def miracleRank(self, repetition: int):
        cubeI = 0 if self.cubeName == 'glowing' else 1
        mult = 12000000 if self.cubeName == 'glowing' else 22000000
        probList = rankUpList[cubeI]

        total = 0

        for _ in range(repetition):
          count = 0
          current = rankIdx[self.startRank]
          target = rankIdx[self.targetRank]
          while current != target:
              count += 1
              rng = random.uniform(0, 100)
              if rng <= probList[current] * 2:
                current += 1
          total += count

        avg = round(total / repetition, 2)
        money = round(mult * avg)
        return f"You used on average {avg} {self.cubeName} cubes to rank up from {self.startRank} to {self.targetRank} during Miracle Time.\nYou spent {money:,} mesos"
            
            



    