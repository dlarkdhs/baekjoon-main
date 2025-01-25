import sys
input = sys.stdin.readline
import math

def sosu(x):
    res = []
    for i in range(2,int(math.sqrt(x))+1):
        if a[i]:
            j = 2
        while i * j <= n:
            a[i*j] = False
            j += 1
    for i in range(2,n+1):
        if a[i]:
            res.append(i)
    return res

n = int(input())
a = [True for _ in range(n+1)]

A = sosu(n)
s = 0
end = 0

count = 0
for start in range(len(A)):
    while s < n and end < len(A):
        s += A[end]
        end += 1
    if s == n:
        count += 1
    s -= A[start]
print(count)