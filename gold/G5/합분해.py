import sys
input = sys.stdin.readline

n,k = map(int,input().split())
cnt = 0
dp = [[1 for i in range(n+1)] for j in range(k+1)]

for i in range(2,k+1):
    for j in range(1,n+1):
        dp[i][j] = (dp[i][j-1]+dp[i-1][j]) % 1000000000
print(dp[k][n])