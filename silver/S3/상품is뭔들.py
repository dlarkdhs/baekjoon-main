import sys
input = sys.stdin.readline
import math

a,b = map(int,input().split())
a,b = int(int(math.isqrt(b))-int(math.isqrt(a))),(b-a)

while math.gcd(a,b) != 1:
    a,b = a//math.gcd(a,b), b//math.gcd(a,b)
if a == 0 or b == 0:
    print(0)
else:
    print(a,'/',b,sep = '')