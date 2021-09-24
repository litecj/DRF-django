from dataclasses import dataclass
# Create your models here.
# from django.db import models

@dataclass
class Calculator(object):
    num1 :int
    num2 :int

    @property
    def num1(self) -> int: return self._num1

    @property
    def num2(self) -> int: return self._num2

    @num1.setter
    def num1(self, num1 :int): self._num1 = num1

    @num2.setter
    def num2(self, num2 :int): self._num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiple(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

    def remain(self):
        return self.num1 % self.num2

@dataclass
class Grade(object):
    kor :int
    eng :int
    math :int

    @property
    def kor(self) -> int: return self._kor

    @kor.setter
    def kor(self, kor :int): self._kor = kor

    @property
    def eng(self) -> int: return self._eng

    @eng.setter
    def eng(self, eng :int): self._eng = eng

    @property
    def math(self) -> int: return self._math

    @math.setter
    def math(self, math :int): self._math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def average(self):
        return float(self.sum() / 3)

    def return_grade(self) -> str:
        aver = self.average()
        if aver >= 90:
            return 'A'
        elif aver >= 80:
            return 'B'
        elif aver >= 70:
            return 'C'
        elif aver >= 60:
            return 'D'
        elif aver >= 50:
            return 'E'
        else:
            return 'F'
        return null