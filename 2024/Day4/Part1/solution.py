from collections import deque

class Solution:

    def __init__(self, path):
        self.path = path
        self.content = self.parse_input()
        self.grid = self.get_the_grid()
        self.word = 'XMAS'
        self.directions = [
            (0, 1), # horizontal-left
            (1, 0), # vertical down
            (1, 1), # diagonal down right
            (-1, 0), # vertical up
            (0, -1), # horizontal-right
            (-1, -1), # diagonal up left
            (-1, 1), # diagonal up right
            (1, -1), # diagonal down left
        ]
    
    def parse_input(self):
        with open(self.path) as f:
            return f.read().strip().splitlines()
    
    def _convert_to_grid(self):
        grid = []
        for line in self.content:
            row = []
            for char in line:
                row.append(char)
            grid.append(row)
        return grid
    
    def get_the_grid(self):
        return self._convert_to_grid()

    def count_the_occurence(self):
        count = 0
        rows, cols = len(self.grid), len(self.grid[0])

        for row in range(rows):
            for col in range(cols):
                for dir in self.directions:
                    count += self.check_in_all_dirs(row, col, dir)
        return count

    def check_in_all_dirs(self, row, col, dir):
        rows, cols = len(self.grid), len(self.grid[0])

        n = len(self.word)

        for i in range(n):
            nr, nc = row + i * dir[0], col + i * dir[1]

            if not(0<= nr < rows and 0<=nc < cols) or self.grid[nr][nc] !=self.word[i]:
                return 0
        return 1



s = Solution('./2024/Day4/input.txt')
print(s.count_the_occurence())
