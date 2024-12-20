
from collections import deque

class Solution:

    def __init__(self, path):
        self.path = path
        self.list_of_arrays = self.parse()
        self.const_array = []

    def parse(self):
        with open(self.path) as file:
            content = file.read().strip().splitlines()

            result = deque()

            for line in content:
                result.append([int(ele) for ele in line.strip().split(' ')])
            return result
    
    def _is_valid_sequence(self, arr):
        return self.__is_decreasing(arr) or self.__is_increasing(arr)

    
    def _is_safe(self, arr):
        return self.__is_decreasing(arr) or self.__is_increasing(arr)
    
    def __is_decreasing(self, arr):

        for i in range(len(arr) - 1):
            di = abs(arr[i] - arr[i + 1])

            if arr[i] < arr[i + 1]:
                return False
            elif not (1 <= di and di <= 3):
                return False
            
        return True

    def __is_increasing(self, arr):
        
        for i in range(len(arr) - 1):
            di = abs(arr[i] - arr[i + 1])

            if arr[i] > arr[i + 1]:
                return False
            elif not (1 <= di and di <= 3):
                return False
        return True

    def __after_removing_one_level(self, arr, asend=False):
        
        for i in range(len(arr)):
            if self._is_valid_sequence(arr[:i] + arr[i + 1:]):
                return True
        return False
    
    def ans(self):
        total = 0
        for arr in self.list_of_arrays:
            self.const_array = arr
            if self._is_valid_sequence(arr) or self.__after_removing_one_level(arr):
                total += 1
        return total


solution = Solution('./Day2/Part2/input.txt')

re = solution.ans()
print('ans: ', re)
