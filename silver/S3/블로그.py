import sys
input = sys.stdin.readline

n,x = map(int,input().split())
arr = list(map(int,input().split()))

res = sum(arr[:x])
m = res
cnt = 1

for i in range(x,n):
    res += arr[i] - arr[i-x]
    if res > m:
        m = res
        cnt = 1
    elif res == m:
        cnt += 1
if m > 0:
    print(m)
    print(cnt)
else:
    print("SAD")