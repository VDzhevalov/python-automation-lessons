import unittest
from lesson_12.homework_12 import photo_paginator

class TestCheckPagePaginatorFunction(unittest.TestCase):

    def test_photo_paginator_raise_TypeError(self):
        except_message = "value should be a number"
        with self.assertRaises(TypeError) as context:
            photo_paginator(amount_of_photos='aa', pages_capacity='o34')
        self.assertEqual(str(context.exception), except_message)

    def test_photo_paginator_can_count_amount_of_pages(self):
        test_parms = [(20, 10, 2), (20, 9, 3), (20, 1, 20)]

        for photos, page_capacity, expected_pages in test_parms:
            with self.subTest(photos=photos, page_capacity=page_capacity, expected_pages=expected_pages):
                actual_pages_amount = photo_paginator(amount_of_photos=photos, pages_capacity=page_capacity)
                self.assertEqual(actual_pages_amount, expected_pages)


if __name__ == '__main__':
    unittest.main()