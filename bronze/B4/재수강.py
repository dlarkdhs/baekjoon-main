import sys
input = sys.stdin.readline

a = input().rstrip()
find = a[0:5]

n = int(input())
cnt = 0
for _ in range(n):
    b = input().rstrip()
    if b[0:5] == find:
        cnt += 1
print(cnt)