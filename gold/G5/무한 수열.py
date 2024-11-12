import sys
input = sys.stdin.readline

def infinite(n):
    if n in dict:
        return dict[n]
    else:
        dict[n] = infinite(n//p)+infinite(n//q)
        return dict[n]

n,p,q = map(int,input().split())
dict = {}
dict[0] = 1
print(infinite(n))