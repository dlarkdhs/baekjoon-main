import sys
input = sys.stdin.readline

n,m = map(int,input().split())
if n - m < 0 or (n - m) % 2 != 0:
    print(-1)
else:
    N = (n+m) // 2
    M = (n - N)
    print(max(N,M), min(N,M))