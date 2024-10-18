import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    n,m = map(int,input().split())
    if n <= 11 or m <= 3:
        print(-1)
    else:
        print(11*m+4)