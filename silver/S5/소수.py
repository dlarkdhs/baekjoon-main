import sys
input = sys.stdin.readline

a,b,n = map(int,input().split())
for i in range(n):
    a %= b
    a *= 10
print(int(a//b))