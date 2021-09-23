from dataclasses import dataclass
# Create your models here.
# from django.db import models

@dataclass
class Calculator(object):
    num1: int
    num2: int

    @property
    def num1(self) -> int: return self.num1
    @property
    def num2(self) -> int: return self.num2
    @num1.setter
    def num1(self, num1): self.num1 = num1
    @num2.setter
    def num2(self, num2): self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiple(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


@dataclass
class Grade(object):

    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return self.sum() / 3

    @staticmethod
    def main():
        kor = int(input('Korean: '))
        eng = int(input('English: '))
        math = int(input('Math: '))
        grade = Grade(kor, eng, math)
        avg = grade.avg()
        if avg >= 90:
            result = 'A'
        elif avg >= 80:
            result = 'B'
        elif avg >= 70:
            result = 'C'
        elif avg >= 60:
            result = 'D'
        elif avg >= 50:
            result = 'E'
        else:
            result = 'F'
        return f'{result}'