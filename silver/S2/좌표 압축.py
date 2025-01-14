import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int,input().split()))
d = {k:i for i,k in enumerate(sorted(set(x)))}

for i in range(n):
    print(d[x[i]],end=" ")