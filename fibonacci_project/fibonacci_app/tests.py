from django.test import TestCase

from fibonacci_app.views import get_nth_fibonacci

class FibonacciTestCase(TestCase):

    def test_6th_fibonacci(self):
        """test cases for fibonacci function"""
        self.assertEqual(get_nth_fibonacci(6), 8)

    def test_1st_fibonacci(self):
        """test cases for fibonacci function"""
        self.assertEqual(get_nth_fibonacci(1), 1)

    def test_2nd_fibonacci(self):
        """test cases for fibonacci function"""
        self.assertEqual(get_nth_fibonacci(2), 1)

    def test_3rd_fibonacci(self):
        """test cases for fibonacci function"""
        self.assertEqual(get_nth_fibonacci(3), 2)
