import sys
input = sys.stdin.readline

n,m = map(int,input().split())

arr = [list(map(int,input().rstrip())) for _ in range(n)]
arr1 = [list(map(int,input().rstrip())) for _ in range(n)]

def change(a,b):
    for x in range(a,a+3):
        for y in range(b,b+3):
            if arr[x][y] == 0:
                arr[x][y] = 1
            else:
                arr[x][y] = 0

cnt = 0
if (n < 3 or m < 3) and arr != arr1:
    cnt = -1

for i in range(n-2):
    for j in range(m-2):
        if arr[i][j] != arr1[i][j]:
            cnt += 1
            change(i,j)

if cnt != -1:
    if arr != arr1:
        cnt = -1
print(cnt)