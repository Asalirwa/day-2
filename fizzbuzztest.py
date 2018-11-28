import unittest

class TestStringMethods(unittest.TestCase):

    def test_fizzbuzz(self):
        self.assertEqual('fizzbuzz(15,30)', 'fizzbuzz')

    def test_isupper(self):
        self.assertTrue('fizzbuzz(15,9)', 'fizz')
     

    def test_split(self):
        self.assertTrue('fizzbuzz(25,4)', 'buzz')

if __name__ == '__main__':
    unittest.main()
