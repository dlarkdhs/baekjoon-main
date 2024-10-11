import sys
input = sys.stdin.readline

t = int(input())
gop = 1
for i in range(t):
    arr = []
    res = []
    n,m = map(int,input().split())
    for _ in range(m):
        arr.append(list(map(int,input().split())))
    for i in range(n):
        for j in range(m):
            gop *= arr[j][i]
        res.append(gop)
        gop = 1
    m = max(res)
    ii = 0
    for i in range(len(res)):
        if m == res[i]:
            ii = i
    print(ii+1)