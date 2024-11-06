import sys
input = sys.stdin.readline

n,w,h,l = map(int,input().split())
res = (w//l) * (h//l)
if n >= res:
    print(res)
else:
    print(n)