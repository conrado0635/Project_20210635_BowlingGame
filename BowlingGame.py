
class BowlingGame:
    def __init__(self):
        """ Create a List named rolls once the BowlingGame is called"""
        self.rolls=[]

    def roll(self,pins):
        """ Method to add pins in a list rolls"""
        self.rolls.append(pins)

    def score(self):
        result = 0
        rollIndex=0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex +=1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                result += self.frameScore(rollIndex)
                rollIndex +=2
        return result

    def isStrike(self, rollIndex):
        """ Method to determine if the first roll is strike,10 points score """
        return self.rolls[rollIndex] == 10
    def isSpare(self, rollIndex):
        """ Method to determine the first roll and second roll awarded a spare """
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    def strikeScore(self,rollIndex):
        """ Method to return result if first and second ball is strike plus 1 spare ball is strike """
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):
        """Method to return score when awarded a spare ball"""
        return  10+ self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        """Method to return score with no strike"""
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
        

