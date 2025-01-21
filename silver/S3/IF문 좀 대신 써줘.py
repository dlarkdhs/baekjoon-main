import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = [input().split() for _ in range(n)]
a.sort(key = lambda x: int(x[1]))

b = [int(input()) for _ in range(m)]

for i in b:
    start = 0
    end = n
    res = 0
    while start <= end:
        mid = (start + end) // 2
        if int(a[mid][1]) >= i:
            res = mid
            end = mid - 1
        else:
            start = mid + 1
    print(a[res][0])