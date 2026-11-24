import unittest
from rectangle import area, perimeter


class RectangleAreaPositiveTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0, 0), 0)
        self.assertEqual(area(0, 5), 0)
        self.assertEqual(area(5, 0), 0)

    def test_area_positive_int(self):
        self.assertEqual(area(5, 10), 50)
        self.assertEqual(area(1, 1), 1)

    def test_area_positive_float(self):
        self.assertAlmostEqual(area(2.5, 4.0), 10.0)
        self.assertAlmostEqual(area(1.5, 2.5), 3.75)


class RectanglePerimeterPositiveTestCase(unittest.TestCase):
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0, 0), 0)
        self.assertEqual(perimeter(0, 5), 10)
        self.assertEqual(perimeter(5, 0), 10)

    def test_perimeter_positive_int(self):
        self.assertEqual(perimeter(5, 10), 30)
        self.assertEqual(perimeter(1, 1), 4)

    def test_perimeter_positive_float(self):
        self.assertAlmostEqual(perimeter(2.5, 4.0), 13.0)
        self.assertAlmostEqual(perimeter(1.5, 2.5), 8.0)


class RectangleAreaNegativeTestCase(unittest.TestCase):
    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            area("5", "10")
        with self.assertRaises(TypeError):  # wrong
            area(5, "10")
        with self.assertRaises(TypeError):  # wrong
            area("5", 10)
        with self.assertRaises(TypeError):
            area(None, 5)
        with self.assertRaises(TypeError):
            area([1, 2], [3, 4])

    def test_area_wrong_args_count(self):
        with self.assertRaises(TypeError):
            area()
        with self.assertRaises(TypeError):
            area(5)
        with self.assertRaises(TypeError):
            area(1, 2, 3)


class RectanglePerimeterNegativeTestCase(unittest.TestCase):
    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError): # wrong
            perimeter("5", "10")
        with self.assertRaises(TypeError): 
            perimeter(5, "10")
        with self.assertRaises(TypeError):
            perimeter("5", 10)
        with self.assertRaises(TypeError):
            perimeter(None, 5)
        with self.assertRaises(TypeError):
            perimeter([1, 2], 3)

    def test_perimeter_wrong_args_count(self):
        with self.assertRaises(TypeError):
            perimeter()
        with self.assertRaises(TypeError):
            perimeter(5)
        with self.assertRaises(TypeError):
            perimeter(1, 2, 3)


if __name__ == "__main__":
    unittest.main()
