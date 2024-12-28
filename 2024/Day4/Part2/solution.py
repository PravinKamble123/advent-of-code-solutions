
class Solution:

    def __init__(self, path):
        self.path = path
        self.content = self.parse_input()
        self.grid = self.get_the_grid()
    
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

    def _is_valid(self, x, y):
        rows, cols = len(self.grid), len(self.grid[0])
        return 0 <= x < rows and 0 <= y < cols

    def _is_x_mas(self, x, y):
        diagonals = [
            [(x-1, y-1), (x, y), (x+1, y+1)],  # Top-left to bottom-right diagonal
            [(x+1, y-1), (x, y), (x-1, y+1)],  # Bottom-left to top-right diagonal
        ]
        for diagonal in diagonals:
            if not all(self._is_valid(dx, dy) for dx, dy in diagonal):
                return False
            chars = [self.grid[dx][dy] for dx, dy in diagonal]
            if chars != ['M', 'A', 'S'] and chars != ['S', 'A', 'M']:
                return False
        return True

    def count_x_mas_patterns(self):
        count = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 'A' and self._is_x_mas(i, j):
                    count += 1
        return count


s = Solution('./2024/Day4/input.txt')
print(s.count_x_mas_patterns())
