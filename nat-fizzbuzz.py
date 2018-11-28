import unittest
from fizzbuzz import *
class MyFirstTests(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(15,30), 'fizzbuzz')