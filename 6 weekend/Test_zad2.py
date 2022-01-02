import unittest
from Zad2 import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self): # wykonuje sie przed kazdym testem
        self.emp1 = Employee("Rysiek","Lubicz",60,200000)
        self.emp2 = Employee("Jerzy","Chojnicki",68,100000)

    def tearDown(self): # po każdym tescie
        self.emp1 = Employee("Rysiek", "Lubicz", 60, 200000)
        self.emp2 = Employee("Jerzy", "Chojnicki", 68, 100000)

    def test_introduce_self(self):
        self.assertEqual(self.emp1.introduce_self(),"My name is Rysiek Lubicz and I am 60 years old")
        self.assertEqual(self.emp2.introduce_self(),"My name is Jerzy Chojnicki and I am 68 years old")

    def test_raise_salary(self):
        self.assertEqual(self.emp1.raise_salary(1.2),240000)
        self.assertEqual(self.emp2.raise_salary(1.2),120000)

    def test_Do_salary_change(self):
        self.assertNotEqual(self.emp1.raise_salary(1.2), 200000)
        self.assertNotEqual(self.emp2.raise_salary(1.2),100000)

    def test_check_age(self):
        self.assertTrue(self.emp1.age > 18)
        self.assertEqual(self.emp1.check_age(),"Adult employee")
        self.assertIs(self.emp1.age,60)
        tab=[]
        i=18
        for i in range(100):
            tab.append(i)
        self.assertIn(self.emp1.age,tab)
        self.assertTrue(self.emp2.age > 18)
        self.assertEqual(self.emp2.check_age(), "Adult employee")
        self.assertIs(self.emp2.age, 68)

    def test_email(self):
        self.assertEqual(self.emp1.get_email(),'RysiekLubicz@company.com')
        self.assertEqual(self.emp2.get_email(),"JerzyChojnicki@company.com")


if __name__ == '__main__':
    unittest.main()
