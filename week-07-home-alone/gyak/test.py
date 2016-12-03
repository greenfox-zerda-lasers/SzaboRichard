import unittest
from exam3  import count_letter_in_string

class TestForExamThree(unittest.TestCase):
    def test_simple_word_and_letter_count(self):
        self.assertEqual(count_letter_in_string("alma", "a"), 2)

    def test_empty_input(self):
        self.assertEqual(count_letter_in_string("", ""), 0)

    def test_number_for_input(self):
        self.assertEqual(count_letter_in_string(12,1), 0)

    def test_string_list_for_input(self):
        self.assertEqual(count_letter_in_string(["stri","ng"], ["ng"]), 0)

if __name__ == '__main__':
    unittest.main()
