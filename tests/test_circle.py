import unittest
import math
from circle import area, perimeter


class CircleAreaPositiveTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_positive_int(self):
        self.assertAlmostEqual(area(5), math.pi * 25)
        self.assertAlmostEqual(area(1), math.pi)

    def test_area_positive_float(self):
        self.assertAlmostEqual(area(2.5), math.pi * 6.25)


class CirclePerimetePositiverTestCase(unittest.TestCase):
    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive_int(self):
        self.assertAlmostEqual(perimeter(5), 10 * math.pi)
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)

    def test_perimeter_positive_float(self):
        self.assertAlmostEqual(perimeter(2.5), 5 * math.pi)


class CircleAreaNegativeTestCase(unittest.TestCase):
    def test_area_invalid_type(self):
        with self.assertRaises(TypeError):
            area("5")
        with self.assertRaises(TypeError):
            area(None)
        with self.assertRaises(TypeError):
            perimeter([1, 2])

    def test_area_wrong_args_count(self):
        with self.assertRaises(TypeError):
            area()
        with self.assertRaises(TypeError):
            area(5, 10)
        with self.assertRaises(TypeError):
            area(1, 2, 3)
    from decimal import Decimal

    def test_area_high_precision_fail(self):
        from decimal import Decimal

        exact_pi = Decimal("3.141592653589793238462643383279")
        self.assertNotEqual(Decimal(str(area(1))), exact_pi)



class CirclePerimeterNegativeTestCase(unittest.TestCase):
    def test_perimeter_invalid_type(self):
        with self.assertRaises(TypeError):
            perimeter("5")
        with self.assertRaises(TypeError):
            perimeter(None)
        with self.assertRaises(TypeError):
            perimeter([1, 2])

    def test_perimeter_wrong_args_count(self):
        with self.assertRaises(TypeError):
            perimeter()
        with self.assertRaises(TypeError):
            perimeter(5, 10)
        with self.assertRaises(TypeError):
            perimeter(1, 2, 3)

    def test_perimeter_high_precision_fail(self):
        from decimal import Decimal
        
        exact_pi = Decimal("3.141592653589793238462643383279")
        self.assertNotEqual(Decimal(str(perimeter(1))), 2 * exact_pi)


if __name__ == "__main__":
    unittest.main()