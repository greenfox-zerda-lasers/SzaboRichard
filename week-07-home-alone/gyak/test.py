import unittest
from exam3 import count_letter_in_string
from examnew4 import greeter

class TestForExamThreeandFour(unittest.TestCase):
    def test_simple_word_and_letter_count(self):
        self.assertEqual(count_letter_in_string("alma", "a"), 2)

    def test_empty_input(self):
        self.assertEqual(count_letter_in_string("", ""), 0)

    def test_number_for_input(self):
        self.assertEqual(count_letter_in_string(12,1), 0)

    def test_string_list_for_input(self):
        self.assertEqual(count_letter_in_string(["stri","ng"], ["ng"]), 0)

    # --------- Example 4 unittest

    def test_greeter_with_empty_input(self):
        self.assertEqual(greeter(''), 'Hello, Mr Nobody!')

    def test_greeter_with_number_input(self):
        self.assertEqual(greeter(3), 'Hello, 3!')

    def test_greeter_with_name_input(self):
        self.assertEqual(greeter('Bela'), 'Hello, Bela!')

    def test_greeter_with_list_input(self):
        self.assertRaises(TypeError, greeter(['string','sdad']))

if __name__ == '__main__':
    unittest.main()
