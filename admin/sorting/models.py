import dataclasses

from django.db import models

# Create your models here.

class Sorting(object):
    def bubble_sort(self):
        A=self
        for i in range(1, len(A)):
            for j in range(0, len(A)-1):
                if A[j] > A[j+1]:
                    A[j], A[j+1] = A[j+1], A[j]

    def merge_sort(self):
        pass

    def quick_sort(self):
        pass



@dataclasses
class Palindrome(object):
    input_string:str

    def str_to_list(payload:str) -> []:
        return [i for i in payload if i.isalnum()]




@dataclasses
class MySum(object):

    start_number : int
    end_number : int

    @property
    def start_number(self)-> int:return self.start_number

    @property
    def end_unmber(self)-> int:return  self.end_number

    def one_to_ten_sum(self):
        # example 1
        sum = 0
        # for i in []:
        for i in range(1, 10 + 1):
            sum += i

        # example 2
        sum = sum(i for i in range(1, 11))
        print(sum(i for i in range(1, 20)))
        print(sum(i for i in range(1, 19)))

        # example 3
        sum = sum(range(1, 11))
        print(sum)

    def one_to_ten_sum_2(self):
        print(sum(range(1, 11)))