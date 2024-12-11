import sys
input = sys.stdin.readline

n = int(input())

cnt = 0
while n - 5 > 0:
    n -= 5
    cnt += 1
print(cnt + 1)