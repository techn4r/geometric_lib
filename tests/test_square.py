import unittest
import math
from square import area, perimeter

class TestAreaSquare(unittest.TestCase):

    def test_area(self):
        a = 5
        expected_area = a * a
        result = area(a)
        self.assertEqual(result, expected_area)

    def test_area_invalid_side(self):
        invalid_sides = [0, -1, -100]
        for side in invalid_sides:
            with self.subTest(side=side):
                with self.assertRaises(ValueError):
                    area(side)

class TestPerimeterSquare(unittest.TestCase):

    def test_perimeter(self):
        a = 7
        expected_perimeter = 4 * a
        result = perimeter(a)
        self.assertEqual(result, expected_perimeter)

    def test_perimeter_invalid_side(self):
        invalid_sides = [0, -1, -100]
        for side in invalid_sides:
            with self.subTest(side=side):
                with self.assertRaises(ValueError):
                    perimeter(side)

if __name__ == '__main__':
    unittest.main()

