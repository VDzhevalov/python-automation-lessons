import pytest
from lesson_12.homework_12 import Rhombus

class TestRombus:

    def test_rhombus_throws_ValueError_when_side_has_invalid_type(self):
        except_message = 'Incorrect value a:  should be a number,  should be great than 0'
        with pytest.raises(ValueError) as context:
            Rhombus('asd', 20)
        assert str(context.value) == except_message

    def test_rhombus_throws_ValueError_when_side_has_wrong_value(self):
        except_message = 'Incorrect value a:  should be a number,  should be great than 0'
        with pytest.raises(ValueError) as context:
            Rhombus(0, 20)
        assert str(context.value) == except_message

    def test_rhombus_ValueError_when_alpha_angle_has_invalid_type(self):
        except_message = 'Incorrect value alpha:  should be a number,  should be great than 0 and less than 180'
        with pytest.raises(ValueError) as context:
            Rhombus(5, 'asd')
        assert str(context.value) == except_message

    @pytest.mark.parametrize("value",[0, 180])
    def test_rhombus_ValueError_when_alpha_angle_has_wrong_value(self, value):
        except_message = 'Incorrect value alpha:  should be a number,  should be great than 0 and less than 180'
        with pytest.raises(ValueError) as context:
                Rhombus(5, value)
        assert str(context.value) == except_message

    @pytest.mark.smoke
    @pytest.mark.parametrize("value, expected", [(1, 179), (90, 90), (179, 1)])
    def test_rhombus_angle_beta_can_be_count(self, value, expected):
        actual = Rhombus(10, value).get_angle_beta()
        assert actual == expected