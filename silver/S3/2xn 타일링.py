import sys
input = sys.stdin.readline

n = int(input())
dp = [0]*1001
dp[0] = 1
dp[1] = 2

if n == 1:
    print(dp[n-1]%10007)
else:
    for i in range(2,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    print(dp[i-1]%10007)