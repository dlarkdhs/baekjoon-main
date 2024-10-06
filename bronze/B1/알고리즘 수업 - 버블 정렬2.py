import sys
input = sys.stdin.readline

n,k = map(int,input().split())
count = 0
a = list(map(int,input().split()))
res = []

for j in range(n):
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
            count += 1
            if count == k:
                res = a.copy()
                break
    if count == k:
        break
if count >= k:
    print(*res)
else:
    print(-1)