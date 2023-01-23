import unittest
from tests import TestCalculations
from tests import TestCalculations2

test_case_1 = unittest.TestLoader().loadTestsFromTestCase(TestCalculations)
test_case_2 = unittest.TestLoader().loadTestsFromTestCase(TestCalculations2)

test_suite_1 = unittest.TestSuite([test_case_1,test_case_2])

unittest.TextTestRunner().run(test_suite_1)