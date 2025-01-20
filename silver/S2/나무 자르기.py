import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))
start, end = 0, max(a)

while start <= end:
    mid = (start + end) // 2
    att = 0
    for i in a:
        if i > mid:
            att += i - mid
    if att >= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)