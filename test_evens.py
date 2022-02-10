import unittest
from evens import even_numbers_of_evens

# to create a test function we need to heritage from the class
# unittest.TestCase

class TestEvens(unittest.TestCase):
    
    def test_thorw_erros_if_list_is_not_passed(self):
        self.assertRaises(TypeError, even_numbers_of_evens, 5)

    def test_for_the_values(self):
        self.assertEqual(even_numbers_of_evens([]), False)
        self.assertEqual(even_numbers_of_evens([4, 2]), True)
        self.assertEqual(even_numbers_of_evens([4]), False)
        self.assertEqual(even_numbers_of_evens([3, 5, 7]), False)


if __name__ == '__main__':
    unittest.main()
