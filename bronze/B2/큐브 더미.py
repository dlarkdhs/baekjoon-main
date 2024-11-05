import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = []

cnt = 0
for i in range(m):
    i,j,k = map(int,input().split())
    a.append([i,j,k])

for i in range(m):
    A = [a[i][0]+1,a[i][1],a[i][2]]
    B = [a[i][0],a[i][1]+1,a[i][2]]
    C = [a[i][0],a[i][1],a[i][2]+1]
    D = [a[i][0]-1,a[i][1],a[i][2]]
    E = [a[i][0],a[i][1]-1,a[i][2]]
    F = [a[i][0],a[i][1],a[i][2]-1]
    if A in a and B in a and C in a and D in a and E in a and F in a:
        cnt += 1
print(cnt)