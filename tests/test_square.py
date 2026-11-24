import unittest
from square import area, perimeter


class SquareAreaPositiveTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_positive_int(self):
        self.assertEqual(area(5), 25)
        self.assertEqual(area(1), 1)

    def test_area_positive_float(self):
        self.assertAlmostEqual(area(2.5), 6.25)


class SquarePerimeterPositiveTestCase(unittest.TestCase):
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive_int(self):
        self.assertEqual(perimeter(5), 20)
        self.assertEqual(perimeter(1), 4)

    def test_perimeter_positive_float(self):
        self.assertAlmostEqual(perimeter(2.5), 10.0)


class SquareAreaNegativeTestCase(unittest.TestCase):
    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            area("5")
        with self.assertRaises(TypeError):
            area(None)
        with self.assertRaises(TypeError):
            area([1, 2])

    def test_area_wrong_args_count(self):
        with self.assertRaises(TypeError):
            area()
        with self.assertRaises(TypeError):
            area(5, 10)
        with self.assertRaises(TypeError):
            area(1, 2, 3)


class SquarePerimeterNegativeTestCase(unittest.TestCase):
    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            perimeter(None)
        with self.assertRaises(TypeError):
            perimeter({"a": 1})
        with self.assertRaises(TypeError):
            perimeter({1, 2})
        with self.assertRaises(TypeError): #wrong
            perimeter([1, 2])

    def test_perimeter_wrong_args_count(self):
        with self.assertRaises(TypeError):
            perimeter()
        with self.assertRaises(TypeError):
            perimeter(5, 10)
        with self.assertRaises(TypeError):
            perimeter(1, 2, 3)


if __name__ == "__main__":
    unittest.main()
