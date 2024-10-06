import sys
input = sys.stdin.readline

n,m = map(int,input().split(' '))
col = [0 for i in range(n)]
row = [0 for i in range(m)]
for i in range(n):
    a = list(map(str,input().strip()))
    for j in range(m):
        if a[j] == 'X':
            col[i] += 1
            row[j] += 1
if col.count(0) > row.count(0):
    print(col.count(0))
else:
    print(row.count(0))