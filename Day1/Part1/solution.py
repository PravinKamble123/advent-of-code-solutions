
from collections import deque

with open(r'./Day1/Part1/input.txt') as file:
    content = file.read().strip().splitlines()
    
    arr1 = deque()
    arr2 = deque()

    for line in content:
        a, _ , _ , b = line.split(' ')
        arr1.append(a)
        arr2.append(b)
    
    arr1 = list(arr1)
    arr2 = list(arr2)

    arr1.sort()
    arr2.sort()

    total = sum([abs(int(a) - int(b)) for a, b in zip(arr1, arr2)])

    print(total)