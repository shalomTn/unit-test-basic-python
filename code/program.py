## assert
# assert should not be used for error handling but for debugging and testing
# assert <condition>, <string-to-be-displayed>

## unittest
# unittest.TestCase class represents one test case as a single unit
#   this allows us to create our own test cases and run multiple tests at once
#   TestCase class provides its own asset methods that are listed as follows:
#           Method	                Checks that
#     assertEqual(a, b)	            a == b
#     assertNotEqual(a, b)	        a != b
#     assertTrue(x)   	        bool(x) is True
#     assertFalse(x)	        bool(x) is False
#     assertIs(a, b)	            a is b
#     assertIsNot(a, b)	        a is not b
#     assertIsNone(x)	        x is None
#     assertIsNotNone(x)	    x is not None
#     assertIn(a, b)	        a in b
#     assertNotIn(a, b)	        a not in b
#     assertIsInstance(a, b)	isinstance(a, b)
#     assertNotIsInstance(a, b)	not isinstance(a, b)
#    these methods can take msg argument for displaying error
class Calculations:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def get_sum(self):
        return self.a +self.b
    def get_difference(self):
        return self.a - self.b
    def get_product(self):
        return self.a * self.b
    def get_quotient(self):
        try:
             self.a/self.b
        except (ZeroDivisionError):
            print("Division by zero")
            return None
        return self.a/self.b
