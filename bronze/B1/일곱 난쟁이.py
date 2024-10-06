import sys
input = sys.stdin.readline

putin = []
for i in range(9):
    a = int(input())
    putin.append(a)
for i in putin:
    for j in putin:
        if sum(putin)-i-j == 100 and i != j:
            putin.remove(i)
            putin.remove(j)
putin.sort()
for i in putin:
    print(i)