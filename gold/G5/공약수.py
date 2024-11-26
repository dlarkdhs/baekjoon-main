import sys
input = sys.stdin.readline
from math import sqrt

a,b = map(int,input().split())
d = b//a

def gcd(x,y):
    if x % y == 0:
        return y
    return gcd(y,x%y)

for i in range(int(sqrt(d)),0,-1):
    j = int(d/i)
    if d % i == 0 and gcd(i,j) == 1:
        print(i*a,j*a)
        break