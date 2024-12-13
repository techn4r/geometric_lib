import unittest
from triangle import area, perimeter

class TestAreaTriangle(unittest.TestCase):

    def test_area(self):
        a, b, c = 3, 4, 5
        expected_area = 6.0
        result = area(a, b, c)
        self.assertAlmostEqual(result, expected_area)

    def test_area_invalid_triangle(self):
        invalid_triangles = [
            (1, 1, 3),
            (1, 2, 3),
            (0, 1, 1),  
            (-1, 1, 1)
        ]
        for sides in invalid_triangles:
            with self.subTest(sides=sides):
                with self.assertRaises(ValueError):
                    area(*sides)

class TestPerimeterTriangle(unittest.TestCase):

    def test_perimeter(self):
        a, b, c = 3, 4, 5
        expected_perimeter = 12
        result = perimeter(a, b, c)
        self.assertEqual(result, expected_perimeter)

    def test_perimeter_invalid_side(self):
        invalid_sides = [(0, 1, 1), (-1, 1, 1)]
        for sides in invalid_sides:
            with self.subTest(sides=sides):
                with self.assertRaises(ValueError):
                    perimeter(*sides)

if __name__ == '__main__':
    unittest.main()

