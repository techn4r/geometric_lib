import unittest
from calculate import calc


class TestCorrectCircle(unittest.TestCase):

    def test_calc_correct_circle_area(self):
        fig = 'circle'
        func = 'area'
        size = [7]
        expected_result = 'area of circle is 153.93804002589985'
        result = calc(fig, func, size)
        self.assertEqual(result, expected_result)

    def test_calc_correct_circle_perimeter(self):
        fig = 'circle'
        func = 'perimeter'
        size = [3]
        expected_result = 'perimeter of circle is 18.84955592153876'
        result = calc(fig, func, size)
        self.assertEqual(result, expected_result)


class TestCircleError(unittest.TestCase):

    def test_calc_circle_invalid_function(self):
        fig = 'circle'
        func = 'oval'
        size = [7]
        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

    def test_calc_circle_invalid_function_and_size(self):
        test_cases = [
            ('circle', 'oval', []),
            ('circle', 'oval', [10, 5])
        ]

        for fig, func, size in test_cases:
            with self.subTest(fig=fig, func=func, size=size):
                with self.assertRaises(ValueError):
                    calc(fig, func, size)

    def test_calc_circle_perimeter_invalid_size(self):
        test_cases = [
            ('circle', 'perimeter', []),
            ('circle', 'perimeter', [10, 5])
        ]

        for fig, func, size in test_cases:
            with self.subTest(fig=fig, func=func, size=size):
                with self.assertRaises(ValueError):
                    calc(fig, func, size)

    def test_calc_circle_area_invalid_size(self):
        test_cases = [
            ('circle', 'area', []),
            ('circle', 'area', [10, 5])
        ]

        for fig, func, size in test_cases:
            with self.subTest(fig=fig, func=func, size=size):
                with self.assertRaises(ValueError):
                    calc(fig, func, size)

    def test_calc_circle_negative_size(self):
        test_cases = [
            ('circle', 'area', [-5]),
            ('circle', 'perimeter', [-7])
        ]

        for fig, func, size in test_cases:
            with self.subTest(fig=fig, func=func, size=size):
                with self.assertRaises(ValueError):
                    calc(fig, func, size)

    def test_calc_circle_zero_size(self):
        test_cases = [
            ('circle', 'area', [0]),
            ('circle', 'perimeter', [0])
        ]

        for fig, func, size in test_cases:
            with self.subTest(fig=fig, func=func, size=size):
                with self.assertRaises(ValueError):
                    calc(fig, func, size)


class TestCorrectSquare(unittest.TestCase):

    def test_calc_correct_square_area(self):
        fig = 'square'
        func = 'area'
        size = [7]
        expected_result = 'area of square is 49'
        result = calc(fig, func, size)
        self.assertEqual(result, expected_result)

    def test_calc_correct_square_perimeter(self):
        fig = 'square'
        func = 'perimeter'
        size = [3]
        expected_result = 'perimeter of square is 12'
        result = calc(fig, func, size)
        self.assertEqual(result, expected_result)


class TestSquareError(unittest.TestCase):

    def test_calc_square_invalid_function(self):
        fig = 'square'
        func = 'oval'
        size = [7]
        with self.assertRaises(ValueError) as context:
            calc(fig, func, size)

    def test_calc_square_invalid_function_and_size(self):
        test_cases = [
            ('square', 'oval', []),
            ('square', 'oval', [10, 5])
        ]

        for fig, func, size in test_cases:
            with self.subTest(fig=fig, func=func, size=size):
                with self.assertRaises(ValueError):
                    calc(fig, func, size)

    def test_calc_square_perimeter_invalid_size(self):
        test_cases = [
            ('square', 'perimeter', []),
            ('square', 'perimeter', [10, 5])
        ]
        for fig, func, size in test_cases:
            with self.subTest(fig=fig, func=func, size=size):
                with self.assertRaises(ValueError):
                    calc(fig, func, size)

    def test_calc_square_area_invalid_size(self):
        test_cases = [
            ('square', 'area', []),
            ('square', 'area', [10, 5])
        ]

        for fig, func, size in test_cases:
            with self.subTest(fig=fig, func=func, size=size):
                with self.assertRaises(ValueError):
                    calc(fig, func, size)

    def test_calc_square_negative_size(self):
        test_cases = [
            ('square', 'area', [-5]),
            ('square', 'perimeter', [-7])
        ]

        for fig, func, size in test_cases:
            with self.subTest(fig=fig, func=func, size=size):
                with self.assertRaises(ValueError):
                    calc(fig, func, size)

    def test_calc_square_zero_size(self):
        test_cases = [
            ('square', 'area', [0]),
            ('square', 'perimeter', [0])
        ]

        for fig, func, size in test_cases:
            with self.subTest(fig=fig, func=func, size=size):
                with self.assertRaises(ValueError):
                    calc(fig, func, size)

    class TestCalcError(unittest.TestCase):

        def test_calc_invalid_figure_area(self):
            fig = 'triangle'
            func = 'area'
            size = [7]
            with self.assertRaises(ValueError) as context:
                calc(fig, func, size)

        def test_calc_invalid_figure_perimeter(self):
            fig = 'triangle'
            func = 'perimeter'
            size = [3]
            with self.assertRaises(ValueError) as context:
                calc(fig, func, size)

        def test_calc_invalid_figure_and_size(self):
            test_cases = [
                ('triangle', 'perimeter', []),
                ('triangle', 'perimeter', [10, 5])
            ]

            for fig, func, size in test_cases:
                with self.subTest(fig=fig, func=func, size=size):
                    with self.assertRaises(ValueError):
                        calc(fig, func, size)

        def test_calc_invalid_figure_and_function(self):
            fig = 'triangle'
            func = 'oval'
            size = [7]
            with self.assertRaises(ValueError) as context:
                calc(fig, func, size)

        def test_calc_invalid_figure_function_size(self):
            test_cases = [
                ('triangle', 'oval', []),
                ('triangle', 'oval', [10, 5])
            ]

            for fig, func, size in test_cases:
                with self.subTest(fig=fig, func=func, size=size):
                    with self.assertRaises(ValueError):
                        calc(fig, func, size)

if __name__ == '__main__':
        unittest.main()
