import sys
input = sys.stdin.readline
from collections import defaultdict

n = int(input())
arr = defaultdict(list)

for _ in range(n):
    a,b = input().split()
    arr[a].append(b)

arr = dict(sorted(arr.items()))
for key in arr:
    A = sorted(arr[key],reverse=True)
    for i in A:
        print(key, i)