import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())
a = list(permutations(range(1,n+1)))
for i in a:
    print(*i)