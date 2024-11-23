import sys
input = sys.stdin.readline

res = 1
a,b = map(int,input().split())

plus = a-1
for _ in range(b):
    res += plus
    plus += (a-2)
print(res)