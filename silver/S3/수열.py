import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = list(map(int,input().split()))

res = sum(arr[:k])
m = res
for i in range(k,n):
    res += arr[i] - arr[i-k]
    if res > m:
        m = res
print(m)