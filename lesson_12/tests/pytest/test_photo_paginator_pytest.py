import pytest
from lesson_12.homework_12 import photo_paginator

class TestPhotoPaginator:

    def test_photo_paginator_raise_TypeError(self):
        except_message = "value should be a number"
        with pytest.raises(TypeError) as context:
            photo_paginator(amount_of_photos='aa', pages_capacity='o34')
        assert str(context.value) == except_message

    @pytest.mark.smoke
    @pytest.mark.parametrize("photos, page_capacity, expected_pages", [(20, 10, 2), (20, 9, 3), (20, 1, 20)])
    def test_photo_paginator_can_count_amount_of_pages(self, photos, page_capacity, expected_pages):
        actual_pages_amount = photo_paginator(amount_of_photos=photos, pages_capacity=page_capacity)
        assert actual_pages_amount == expected_pages
