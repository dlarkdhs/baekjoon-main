import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    
    cnt = 0
    for i in a:
        first,end = 0, m-1
        while first <= end:
            mid = (first+end)//2
            if b[mid] < i:
                first = mid + 1
            else:
                end = mid - 1
        cnt += first
    print(cnt)