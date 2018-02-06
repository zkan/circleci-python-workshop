import unittest


def fizzbuzz(number):
    if number % 3 == 0:
        return 'fizz'


class FizzBuzzTest(unittest.TestCase):
    def test_input_3_should_get_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, 'fizz')

    def test_input_6_should_get_fizz(self):
        result = fizzbuzz(6)
        self.assertEqual(result, 'fizz')


unittest.main()
