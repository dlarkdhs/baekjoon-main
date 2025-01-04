import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    cnt = 1
    res = []
    n = int(input())
    for _ in range(n):
        a,b = map(int,input().split())
        res.append([a,b])
    res.sort()
    mb = res[0][1]
    res.pop(0)
    for i in range(n-1):
        if res[i][1] < mb:
            cnt += 1
            mb = res[i][1]
    print(cnt)