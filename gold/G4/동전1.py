import sys
input = sys.stdin.readline

n,k = map(int,input().split())
a = []
for _ in range(n):
    a.append(int(input()))

dp = [0 for _ in range(k+1)]
dp[0] = 1

for i in a:
    for j in range(i,k+1):
        dp[j] += dp[j-i]
print(dp[k])