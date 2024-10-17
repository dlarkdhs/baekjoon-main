import sys
input = sys.stdin.readline

a,b = map(int,input().split())
if b >= a:
    print(a+a-1)
else:
    print(b+b+1)