import sys
input = sys.stdin.readline

n = int(input())
A = list()
result = -1
for i in range(n):
    a = input().rstrip()
    A.append(a)
for i in A:
    if 'anj' == i:
        result = 0
print("뭐야;") if result == 0 else print("뭐야?")