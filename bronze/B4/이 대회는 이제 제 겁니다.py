import sys
input = sys.stdin.readline

a,p,c = map(int,input().split())
if a+c > p:
    print(a+c)
else:
    print(p)