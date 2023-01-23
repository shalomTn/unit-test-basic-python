# unit-testing-basic-python

## unittest.TestCase
To conduct unit testing in python import the unittest module and create a new subclass of unittest.TestCase. All the methods in this class beginning with 'test' will be recognized as a test method with an assertion

## TestCase.setUp() Or setUpClass
TestCase.setUp(): This method is called before every test.
@classmethod TestCase.setUpClass(): This method runs once before testing the class' test method

## testing every test
Note that tests/test.py and tests/test2.py do not run independently but may run when we use the command
>python -m unittest

