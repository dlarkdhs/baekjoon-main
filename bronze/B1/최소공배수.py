import sys
input = sys.stdin.readline
from math import *

t = int(input())

for _ in range(t):
    a,b = map(int,input().split())
    print(lcm(a,b))