import sys
input = sys.stdin.readline

n = int(input())
T = []
P = []
for _ in range(n):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)

dp = [0]*(n+2)

for i in range(n,0,-1):
    if i+T[i-1] <= n+1:
        dp[i] = max(dp[i+1],P[i-1]+dp[i+T[i-1]])
    else:
        dp[i] = dp[i+1]
print(dp[1])