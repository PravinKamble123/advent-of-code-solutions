import re
from collections import deque

class Solution:

    def __init__(self, path):
        self.path = path
        self.parse_result = self.parse_input()
    
    def parse_input(self):

        with open(self.path) as f:
            content = f.read().strip()
            return content

    def _get_target_str(self):
        valid = deque()
        idx = 0
        while idx < len(self.parse_result):
            if self.parse_result[idx:idx+7] == "don't()":
                while idx < len(self.parse_result) and self.parse_result[idx:idx+4] != 'do()':
                    idx += 1
                idx += 4
                while idx < len(self.parse_result) and self.parse_result[idx:idx+7] != "don't()":
                    valid.append(self.parse_result[idx])
                    idx += 1
            elif self.parse_result[idx:idx+4] == "mul(":
                while idx < len(self.parse_result) and self.parse_result[idx] != ")":
                    valid.append(self.parse_result[idx])
                    idx += 1
                
                if idx < len(self.parse_result):
                    valid.append(self.parse_result[idx])
            else:
                idx += 1
        return "".join(list(valid))

    def ans(self):
        target_str = self._get_target_str()
        pattern = r"mul\(\d+,\d+\)"
        matches = re.findall(pattern, target_str)
        total = 0
        for match in matches:
            _ , digits = match.split('mul')
            array = "".join("".join(digits.split('(')).split(')')).split(',')
            prod = 1
            for ele in array:
                prod *= int(ele)
            
            total += prod
        
        return total



solution = Solution('./Day3/Part1/input.txt')
ans = solution.ans()

print("Answer is ", ans)