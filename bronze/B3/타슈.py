import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

res = 0
for i in range(n):
    res += abs(a[i]-b[i])
print(res//2)