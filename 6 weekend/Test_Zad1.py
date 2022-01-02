import  unittest
import  Zad1_skrypt as Skrypt

class TestIssues(unittest.TestCase):

    def test_add(self):
        result_add = Skrypt.add(10, 5)
        self.assertEqual(result_add, 15)
    def test_subtract(self):
        result_subtract = Skrypt.subtract(10, 5)
        self.assertEqual(result_subtract,5)
    def test_multipy(self):
        result_multiply = Skrypt.multiply(10, 5)
        self.assertEqual(result_multiply,50)
    def test_divide(self):
        result_divide = Skrypt.divide(10, 5)
        self.assertEqual(result_divide, 2)
        self.assertRaises(ValueError,Skrypt.divide(10,0))


if __name__ == '__main__':
    unittest.main()
