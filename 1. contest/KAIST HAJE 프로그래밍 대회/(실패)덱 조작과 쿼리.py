import sys
input = sys.stdin.readline
from collections import deque

d = deque()
restore = []
n = int(input())

for i in range(n):
    temp = input().strip().split()
    command = temp[0]
    
    if command == "push":
        d.appendleft(int(temp[1]))
        restore.append(d.copy())
    elif command == "pop":
        d.popleft()
        restore.append(d.copy())
    elif command == "restore":
        i = int(temp[1])
        d = restore[i]
    elif command == "print":
        if len(d) != 0:
            print(sum(d))
            restore.append(d.copy())
        else:
            print(0)
            restore.append(d.copy())