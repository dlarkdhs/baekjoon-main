import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    for i in range(1,n):
        if i**2 <= n:
            cnt += 1
        if i**2 > n:
            break
    print(cnt)