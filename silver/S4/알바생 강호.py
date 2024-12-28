import sys
input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)

s = 0
j = 0
for i in arr:
    if i-j < 0:
        continue
    s += i-j
    j += 1
print(s)