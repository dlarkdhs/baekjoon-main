import sys
input = sys.stdin.readline

r,c = map(int,input().split())
a = [list(map(str,input().rstrip()))for _ in range(c)]

res = [0]*5
for i in range(r-1):
    for j in range(c-1):
        cnt = 0
        if a[i][j] == "#" or a[i][j+1] == "#" or a[i+1][j] == "#" or a[i+1][j+1] == "#":
            continue
        if a[i][j] == "X":
            cnt += 1
        if a[i][j+1] == "X":
            cnt += 1
        if a[i+1][j] == "X":
            cnt += 1
        if a[i+1][j+1] == "X":
            cnt += 1
        res[cnt] += 1

for i in res:
    print(i)