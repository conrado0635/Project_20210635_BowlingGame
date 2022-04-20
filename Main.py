
import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):
    """Test Case Method"""
    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        """Iterate 20times and initialized value to zero.And verify that the total score is equal to zero."""
        self.rollMany(0,20) 
        print(self.game.score) 
        assert self.game.score()==0
    def testAllOnes(self):
        """Iterate 20times and initialized value to one.And verify that the total score is equal to 20. """
        self.rollMany(1, 20)
        print(self.game.score)
        assert self.game.score()==20
    def testOneSpare(self):
        """Verify the total frame score with no strike plus spare ball is equal 16.
        Parameter example: (frame1 ball1 +(frame2 ball1+frame2 ball2)+frame2 ball2;Total Score =(5 + (5+3) +3)
        """
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        assert self.game.score()==16
    def testOneStrike(self):
        """Verify the total frame score with one strike is equal 24.
        Parameter example:frame1=strike ball(10pins)+frame2;frame2=(frame2 ball1+frame2 ball2);Total Score=(10 + (4+3) +(4+3))
        """
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,16)
        assert self.game.score()==24
    def testPerfectGame(self):
        """Test a perfect strike, perpect 10 points for all rolls
        Parameter example:(i=0,pins=10,rolls=12,Score:(10+10+10,10+10+10...n=12)"""
        self.rollMany(10,12)
        assert self.game.score()==300
    def testAllSpare(self):
        self.rollMany(5,21)
        assert self.game.score()==150
    def rollMany(self, pins,rolls):
        """Iterate from i to rolls and append pins to List roll.
        Parameter example:(i =0,pins=5,roll=10,roll=[5,5,5,5,5,5,5,5,5,5]) 
        """
        for i in range(rolls):
           self.game.roll(pins)
           


if __name__=='__main__':
    unittest.main()


