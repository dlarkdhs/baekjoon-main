import sys
input = sys.stdin.readline

n = int(input())
dp = [1,3]+[0]*(n-2)
if n < 2:
    print(dp[n-1])
else:
    for i in range(2,n):
        dp[i] = 2*dp[i-2]+dp[i-1]
    print(dp[n-1]%10007)