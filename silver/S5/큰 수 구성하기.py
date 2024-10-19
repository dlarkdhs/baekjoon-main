import sys
input = sys.stdin.readline
from itertools import product

n,k = map(int,input().split())
N = len(str(n))
a = list(input().split())

while True:
    tmp = list(product(a, repeat=N))
    res = []
    for i in tmp:
        if int("".join(i)) <= n:
            res.append(int("".join(i)))
    if len(res) >= 1:
        print(max(res))
        break
    else:
        N -= 1