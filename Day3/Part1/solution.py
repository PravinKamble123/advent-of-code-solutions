import re

class Solution:

    def __init__(self, path):
        self.path = path
        self.parse_result = self.parse_input()
    

    def parse_input(self):

        with open(self.path) as f:
            content = f.read().strip()
            return content


    def ans(self):
        pattern = r"mul\(\d+,\d+\)"
        matches = re.findall(pattern, self.parse_result)
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