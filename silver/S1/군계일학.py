import sys
input = sys.stdin.readline

n = int(input())
a = [0]+list(map(int,input().split()))
dp = [0]*1000001

for i in range(1,n+1):
    N = a[i]
    dp[N] = max(dp[N],dp[N-1]+1)
print(max(dp))