import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))

start, end = max(a), sum(a)

res = 10**9
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    s = 0
    for i in range(n):
        if s+a[i] <= mid:
            s += a[i]
        else:
            cnt += 1
            s = a[i]
        if cnt > m:
            break
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
        if mid >= start:
            res = min(res,mid)
print(res)