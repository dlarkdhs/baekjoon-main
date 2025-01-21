import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
m = int(input())

start,end = 0, max(a)
while start <= end:
    mid = (start + end) // 2
    s = 0
    for i in a:
        if i >= mid:
            s += mid
        else:
            s += i
    if s <= m:
        start = mid + 1
    else:
        end = mid - 1
print(end)