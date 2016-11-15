import unittest
from ricsi_work import anagramm, count_letters

class FirstUnitTest(unittest.TestCase):
    def test_set_anagramm_input(self):
        self.assertTrue(anagramm("alma","lama"))

    def test_set_anagramm_input_not_anag(self):
        self.assertFalse(anagramm("1","banán"))

    def test_set_anagramm_input_number_string(self):
        self.assertRaises(AttributeError,anagramm,311 ,123)

    def test_set_anagramm_input_UpperCase(self):
        self.assertTrue(anagramm('ALMA', 'alma'))

    def test_set_anagramm_input_moreChar(self):
        self.assertFalse(anagramm('alma A', 'a lma'))

    def test_set_anagramm_input_whiteSpace(self):
        self.assertTrue(anagramm('alm a', 'a lma'))

    # -----------------

    def test_set_count_letters_input_number_string(self):
        self.assertRaises(AttributeError, count_letters, 311)

    def test_set_count_letters_input_whiteSpace(self):
        self.assertTrue(count_letters('AAAAadsasdaslmfkslkdf'))

if __name__ == '__main__':
    unittest.main()
