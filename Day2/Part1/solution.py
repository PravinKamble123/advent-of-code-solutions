
from collections import deque, Counter

class Solution:

    def __init__(self, path):
        self.path = path
        self.list_of_arrays = self.parse()

    def parse(self):
        with open(self.path) as file:
            content = file.read().strip().splitlines()

            result = deque()

            for line in content:
                result.append([int(ele) for ele in line.strip().split(' ')])
            return result
    
    def _is_safe(self, arr):
        return self.is_decreasing(arr) or self.is_increasing(arr)
    
    def is_decreasing(self, arr):

        for i in range(len(arr) - 1):
            di = abs(arr[i] - arr[i + 1])
            if arr[i] < arr[i + 1]:
                return False
            elif not (1 <= di and di <= 3):
                return False
        return True

    def is_increasing(self, arr):

        for i in range(len(arr) - 1):
            di = abs(arr[i] - arr[i + 1])
            if arr[i] > arr[i + 1]:
                return False
            elif not (1 <= di and di <= 3):
                return False
        return True
    
    
    def ans(self):
        total = 0
        for arr in self.list_of_arrays:
            if self._is_safe(arr):
                total += 1
        return total


solution = Solution('./Day2/Part1/input.txt')

re = solution.ans()
print(re)
