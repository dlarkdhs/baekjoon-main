import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = []
res = []
for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            res.append([i,j])
print(abs(res[1][0]-res[0][0])+abs(res[1][1]-res[0][1]))