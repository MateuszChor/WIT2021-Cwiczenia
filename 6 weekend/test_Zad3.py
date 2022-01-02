import unittest
import Zad3 as zad


class MyTestCase(unittest.TestCase):
    def test_isnumeric(self):
        for i in range(1000):
            self.assertEqual(zad.is_numeric(i),True)
            self.assertTrue(zad.is_numeric(i))

    def test_isNegativ(self):
        self.assertEqual(zad.is_negative(10),False)
        self.assertFalse(zad.is_negative(3))

    def test_calculate_savings(self):
        self.assertEqual(zad.calculate_savings(10000,1000,100),20800)
        self.assertRaises(ValueError,zad.calculate_savings("a","b","c"))
        self.assertRaises(ValueError,zad.calculate_savings(-100,-10,-1))

if __name__ == '__main__':
    unittest.main()
