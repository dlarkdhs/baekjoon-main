import sys
input = sys.stdin.readline

n = int(input())
a,b = 0,1

res = 1
for _ in range(n-2):
    a,b = b,a+b
    res += a
if n == 0:
    print(0)
else:
    print(res)