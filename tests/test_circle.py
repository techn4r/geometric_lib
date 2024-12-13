import unittest
import math
from circle import area, perimeter


class TestAreaCircle(unittest.TestCase):

    def test_area(self):
        r = 5
        expected_area = math.pi * r * r
        result = area(r)
        self.assertAlmostEqual(result, expected_area)

    def test_area_invalid_radius(self):
        invalid_radius = [0, -1, -100]
        for radius in invalid_radius:
            with self.subTest(radius=radius):
                with self.assertRaises(ValueError):
                    area(radius)


class TestPerimeterCircle(unittest.TestCase):

    def test_perimeter(self):
        r = 7
        expected_perimeter = 2 * math.pi * r
        result = perimeter(r)
        self.assertAlmostEqual(result, expected_perimeter)

    def test_perimeter_invalid_radius(self):
        invalid_radius = [0, -1, -100]
        for radius in invalid_radius:
            with self.subTest(radius=radius):
                with self.assertRaises(ValueError):
                    perimeter(radius)


if __name__ == '__main__':
    unittest.main()
