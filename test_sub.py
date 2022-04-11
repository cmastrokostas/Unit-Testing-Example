import unittest 
from sub import Operation

class TestSub(unittest.TestCase):
    def test_sub(self):
        self.assertAlmostEqual(Operation.sub(1,1) , "ZERO" )
        self.assertAlmostEqual(Operation.sub(5,1) , "POSITIVE" )  
        self.assertAlmostEqual(Operation.sub(7,1) , "POSITIVE" )
        self.assertAlmostEqual(Operation.sub(3,2) , "POSITIVE" )
        self.assertAlmostEqual(Operation.sub(-3,2), "NEGATIVE" )
        self.assertAlmostEqual(Operation.sub(1,5) , "NEGATIVE" )
if __name__ == "__main__":
    unittest.main()