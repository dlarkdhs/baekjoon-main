import sys
input = sys.stdin.readline
from itertools import combinations

n,m = map(int,input().split())
arr = list(list(map(int,input().split())) for _ in range(n))
result = 999999
num1 = []
num2 = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            num1.append([i,j])
        elif arr[i][j] == 2:
            num2.append([i,j])

for i in combinations(num2,m):
    tmp = 0
    for j in num1:
        res = 999
        for k in range(m):
            res = min(res,abs(j[0]-i[k][0])+abs(j[1]-i[k][1]))
        tmp += res
    result = min(result,tmp)
print(result)