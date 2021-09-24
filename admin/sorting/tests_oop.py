import unittest
from admin.sorting.models_oop import Grade, Calculator

class TestCalculator(unittest.TestCase):
    cal = Calculator()
    cal.num1 = 8
    cal.num2 = 5

    def test_add(self):
        self.assertEqual(self.cal.add(), 13)

    def test_sub(self):
        self.assertEqual(self.cal.subtract(), 3)

    def test_multi(self):
        self.assertEqual(self.cal.multiple(), 40)

    def test_div(self):
        self.assertEqual(self.cal.divide(), 1.6)

    def test_mod(self):
        self.assertEqual(self.cal.remain(), 3)


class TestGrade(unittest.TestCase):

    def test_grade(self):
        grade = Grade()
        grade.kor = 92
        grade.eng = 88
        grade.math = 90
        print(f'grade is {grade.return_grade()}')
        self.assertEqual(grade.return_grade(), 'c')


class TestPerson(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
