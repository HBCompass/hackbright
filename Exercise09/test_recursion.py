import unittest
import math

from recursion import *

class TestRecursionOperations(unittest.TestCase):

    def setUp(self):
        self.numbers1 = [5, 2, 1, 4, 3, 6]
        self.numbers2 = [5, 24, 48, 88]
        self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                       'Sep', 'Oct', 'Nov', 'Dec']


    ### Tests for recursion.py ###
    def test_multiply_list(self):
        self.assertEqual(multiply_list(self.numbers1), 720)
        self.assertEqual(multiply_list(self.numbers2), 506880)

    def test_factorial(self):
        self.assertEqual(factorial(1), math.factorial(1))
        self.assertEqual(factorial(2), math.factorial(2))
        self.assertEqual(factorial(3), math.factorial(3))
        self.assertEqual(factorial(4), math.factorial(4))
        self.assertEqual(factorial(5), math.factorial(5))
        self.assertEqual(factorial(10), math.factorial(10))
        self.assertEqual(factorial(20), math.factorial(20))

    def test_count_list(self):
        self.assertEqual(count_list(self.numbers1), len(self.numbers1))
        self.assertEqual(count_list(self.numbers2), len(self.numbers2))
        self.assertEqual(count_list(self.months),   len(self.months))

    def test_sum_list(self):
        self.assertEqual(sum_list(self.numbers1), sum(self.numbers1))
        self.assertEqual(sum_list(self.numbers2), sum(self.numbers2))

    def test_reverse_list(self):
        self.assertEqual(reverse(self.numbers1), self.numbers1[::-1])
        self.assertEqual(reverse(self.numbers2), self.numbers2[::-1])
        self.assertEqual(reverse(self.months), self.months[::-1])

    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(9), 34)

    def test_find(self):
        self.assertEqual(find(self.numbers1, 4), 4)
        self.assertEqual(find(self.numbers1, 5), 5)
        self.assertEqual(find(self.months, "Jan"), "Jan")
        self.assertEqual(find(self.months, "Feb"), "Feb")
        self.assertEqual(find(self.months, "Dec"), "Dec")
        self.assertEqual(find(self.months, "Jul"), "Jul")
        self.assertEqual(find(self.months, "Hex"), None)

    def test_palindrome(self):
        self.assertTrue(palindrome("radar"))
        self.assertTrue(palindrome("racecar"))
        self.assertTrue(palindrome("poop"))
        self.assertFalse(palindrome("palindrome"))
        self.assertFalse(palindrome("abcdecba"))

    def test_fold_paper(self):
        self.assertEqual(fold_paper(8.5, 11, 1), (8.5, 11.0/2))
        self.assertEqual(fold_paper(8.5, 11, 2), (8.5/2, 11.0/2))
        self.assertEqual(fold_paper(8.5, 11, 3), (8.5/2, 11.0/2/2))
        self.assertEqual(fold_paper(8.5, 11, 4), (8.5/2/2, 11.0/2/2))
        self.assertEqual(fold_paper(8.5, 11, 5), (8.5/2/2, 11.0/2/2/2))

        self.assertEqual(fold_paper(10, 10, 2), (10.0/2, 10.0/2))
        self.assertEqual(fold_paper(10, 10, 4), (10.0/2/2, 10.0/2/2))


if __name__ == '__main__':
    unittest.main()
