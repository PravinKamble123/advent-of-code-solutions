
class Solution:

    def __init__(self, path):
        self.path = path
        self.grid = self.get_the_grid()
        self.visited = set()

    def _parse_the_input(self):
        with open(self.path) as f:
            return f.read().strip().splitlines()

    def get_the_grid(self):
        lines = self._parse_the_input()
        return [list(line) for line in lines]

    def go_up(self, row, col):
        while row >= 0 and self.grid[row][col] != "#":
            self.visited.add((row, col))
            self.grid[row][col] = 'x'
            row -= 1
        if row >= 0 and self.grid[row][col] == '#':
            self.go_right(row + 1, col)
        else:
            return

    def go_right(self, row, col):
        while col < len(self.grid[0]) and self.grid[row][col] != "#":
            self.visited.add((row, col))
            self.grid[row][col] = 'x'
            col += 1
        
        if col < len(self.grid[0]) and self.grid[row][col] == '#':
            self.go_down(row, col - 1)
        else:
            return

    def go_down(self, row, col):
        while row < len(self.grid) and self.grid[row][col] != "#":
            self.visited.add((row, col))
            self.grid[row][col] = 'x'
            row += 1
        
        if row < len(self.grid) and self.grid[row][col] == '#':
            self.go_left(row - 1, col)
        else:
            return

    def go_left(self, row, col):
        while col >= 0 and self.grid[row][col] != "#":
            self.visited.add((row, col))
            self.grid[row][col] = 'x'
            col -= 1
        
        if col >= 0 and self.grid[row][col] == '#':
            self.go_up(row, col + 1)
        else:
            return

    def explore(self):
        rows, cols = len(self.grid), len(self.grid[0])
        
        for row in range(rows):
            for col in range(cols):
                if self.grid[row][col] == "^":
                    self.visited.add((row, col))
                    self.go_up(row, col)
                    break
        return len(self.visited)

s = Solution('./2024/Day6/input.txt')
explored = s.explore()
print("answer : ", explored)
