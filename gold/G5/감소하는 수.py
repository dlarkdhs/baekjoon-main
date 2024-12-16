import sys
input = sys.stdin.readline
from itertools import combinations

res = []
n = int(input())

for i in range(1,11):
    for j in combinations(range(10),i):
        a = sorted(list(j),reverse=True)
        res.append(int("".join(map(str, a))))
res.sort()
print(res[n] if len(res) > n else -1)