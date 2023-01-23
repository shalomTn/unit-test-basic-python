import unittest
from code.program  import Calculations

class TestCalculations2(unittest.TestCase):
    #when we run unittest.main()
    # 1. @classmethod setUpClass function will run 
    # 2. for all the functions (say test_f...()) whose name start with 'test' 
    #    a. setUp() will run
    #    b. test_f..() will run
    def setUp(self) -> None:
        self.calculation=Calculations(-10,19)
        #instead of this we can also use the @classmethod setUpClass
    def test_sum(self):
        self.assertEqual(self.calculation.get_sum(),9,'The sum is wrong')
    def test_diff(self):
        self.assertEqual(self.calculation.get_difference(),-29,'The difference is wrong')
    def test_product(self):
        self.assertEqual(self.calculation.get_product(),-190,'The product is wrong')
    def test_quotient(self):
        self.assertEqual(self.calculation.get_quotient(),-10/19,'The quotient is wrong')
    def test_quotient_zero(self):
        temp=Calculations(8,0)
        self.assertEqual(temp.get_quotient(),None,'The quotient is wrong')
#if __name__ == '__main__':
#    unittest.main()
#this is required if you are indivually doing it
