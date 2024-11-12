import sys
input = sys.stdin.readline

t = int(input())

res = []
a,b = 0,1
for i in range(41):
    res.append(a)
    a,b = b,a+b

for _ in range(t):
    n = int(input())
    if n == 0:
        print("1 0")
    else:
        print(res[n-1],res[n])