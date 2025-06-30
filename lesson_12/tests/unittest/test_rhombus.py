import unittest
from lesson_12.homework_12 import Rhombus

class TestRhombus(unittest.TestCase):

    def test_rhombus_throws_ValueError_when_side_has_invalid_type(self):
        except_message = 'Incorrect value a:  should be a number,  should be great than 0'
        with self.assertRaises(ValueError) as context:
            Rhombus('asd', 20)
        self.assertEqual(str(context.exception), except_message)

    def test_rhombus_throws_ValueError_when_side_has_wrong_value(self):
        except_message = 'Incorrect value a:  should be a number,  should be great than 0'
        with self.assertRaises(ValueError) as context:
            Rhombus(0, 20)
        self.assertEqual(str(context.exception), except_message)

    def test_rhombus_ValueError_when_alpha_angle_has_invalid_type(self):
        except_message = 'Incorrect value alpha:  should be a number,  should be great than 0 and less than 180'
        with self.assertRaises(ValueError) as context:
            Rhombus(5, 'asd')
        self.assertEqual(str(context.exception), except_message)

    def test_rhombus_ValueError_when_alpha_angle_has_wrong_value(self):
        except_message = 'Incorrect value alpha:  should be a number,  should be great than 0 and less than 180'
        test_parms = [0, 180]

        for value in test_parms:
            with self.subTest(value=value):
                with self.assertRaises(ValueError) as context:
                    Rhombus(5, value)
                self.assertEqual(str(context.exception), except_message)

    def test_rhombus_angle_beta_can_be_count(self):
        test_parms = [(1, 179), (90, 90), (179, 1)]

        for value, expected in test_parms:
            with self.subTest(value=value, expected=expected):
                actual = Rhombus(10, value).get_angle_beta()
                self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()