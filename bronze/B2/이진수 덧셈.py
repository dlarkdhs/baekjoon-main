import sys
input = sys.stdin.readline

a,b = map(str,input().split())
a = int(a,2)
b = int(b,2)
res = bin(a+b)
print(res[2::])