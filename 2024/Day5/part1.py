from collections import defaultdict

class Solution:

    def __init__(self, path):
        self.path = path
        self.content = self.read_file()
        self.records, self.updates = self.split_in_two_parts()
        self.graph = self.build_graph()

    def read_file(self):
        with open(self.path) as f:
            return f.read().strip().splitlines()
    
    def split_in_two_parts(self):
        digits = []
        updates = []
        found = False
        for line in self.content:
            if not found:
                if line == "":
                    found = True
                    continue
                else:
                    digits.append(line)
            if found: 
                updates.append(line)

        return digits, updates
    
    def build_graph(self):
        
        graph = defaultdict(set)

        for record in self.records:
            a, b = record.split("|")
            graph[a].add(b)

    def is_valid_sequence(self):
        
        for update in s.updates:
            pass


s = Solution('./2024/Day5/input.txt')
# s.build_graph()

