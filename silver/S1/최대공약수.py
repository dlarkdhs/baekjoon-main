import sys
input = sys.stdin.readline
import math

a,b = map(int,input().split())
res = math.gcd(a,b)
print('1'*res)