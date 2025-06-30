import unittest
from lesson_12.homework_12 import sum_two_num

class TestCheckSumTwoNumFunction(unittest.TestCase):

    def test_two_positive_num_summ_is_correct(self):
        self.assertTrue(sum_two_num(5, 5) == 10)

    def test_two_negative_sum_is_correct(self):
        self.assertTrue(sum_two_num(-1, -3) == -4)

    def test_sum_returns_zero_when_attribute_is_not_a_number(self):
        self.assertTrue(sum_two_num('aa','bb') == 0)

if __name__ == '__main__':
    unittest.main()

