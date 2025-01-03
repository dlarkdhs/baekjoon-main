import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

prefix_sum = [0]*n
prefix_sum[0] = a[0]

for i in range(1,n):
    prefix_sum[i] = prefix_sum[i-1] + a[i]

for _ in range(m):
    start,end = map(int,input().split())
    if start == 1:
        print(prefix_sum[end-1])
    else:
        print(prefix_sum[end-1]-prefix_sum[start-2])