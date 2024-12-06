import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

arr = [list(map(int,input().split())) for _ in range(k)]

for i,j in arr:
    res = min(i-1,j-1,n-i,n-j)
    color = (res % 3) + 1
    print(color)