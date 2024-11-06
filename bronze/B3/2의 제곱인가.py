import sys
input = sys.stdin.readline
import math

n = int(input())

if n != 1:
    a = math.log(n,2)
    if not a - int(a):
        print(1)
    else:
        print(0)
else:
    print(1)