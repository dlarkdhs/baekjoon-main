import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = list(map(int,input().split()))

i,j,cnt,total = 0,0,0,0
while True:
    if total >= m:
        total -= a[i]
        i += 1
    elif j == n:
        break
    else:
        total += a[j]
        j += 1
    if total == m:
        cnt += 1
print(cnt)