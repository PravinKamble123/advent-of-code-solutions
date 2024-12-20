
from collections import Counter, deque

class Solution:

    def __init__(self, file_path):
        self.arr1, self.arr2 = self.parse_input(file_path)
    

    def parse_input(self, path):

        with open(path) as file:
            content = file.read().strip().splitlines()
            nums1 = deque()
            nums2 = deque()

            for line in content:
                a, _ , _, b = line.split(' ')
                nums1.append(a)
                nums2.append(b)
            arr1 = list(nums1)
            arr2 = list(nums2)

            arr1.sort()
            arr2.sort()
            return arr1, arr2
            
    def ans(self):
        counter = Counter(self.arr2)
        ans = 0
        for num in self.arr1:
            ans += (int(num) * int(counter.get(num, 0)))
        return ans


sol = Solution(f'./Day1/Part2/input.txt')
ans = sol.ans()

print(ans)
