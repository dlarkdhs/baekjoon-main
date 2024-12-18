import sys
input = sys.stdin.readline

n = int(input())
dp = [0,1]

if n == 0:
    print(0)
else:
    for i in range(2,n+1):
        ans = dp[i-1] + dp[i-2]
        dp.append(ans)
    print(dp[-1])