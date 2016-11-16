import unittest
from f01 import num_divide
from f02 import file_reader
from f03 import Person

class WensdayUnitTest(unittest.TestCase):

    def test_division_by_zero_except(self):
        self.assertEqual(num_divide(0),"fail")

    def test_division_by_string_except(self):
        self.assertEqual(num_divide("asdasdasf"),"please give me a number")

    # def test_num_divide_by_string(self):
    #     self.assertRaises(TypeError, num_divide, "dsfjhjsdfhl")

    # ------------------ 2. pelda alul -----------------------

    def test_file_reader_test_case_without_file(self):
        self.assertEqual(file_reader(""),"0")

    # ///////////// 3. pelda ////////////////

    def test_Person_birthday_0(self):
        self.assertRaises(ValueError, Person,"name",0)

if __name__ == '__main__':
    unittest.main()
