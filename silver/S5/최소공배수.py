import sys
input = sys.stdin.readline
import math

a,b = map(int,input().split())
res = math.lcm(a,b)
print(res)