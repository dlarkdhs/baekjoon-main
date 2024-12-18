import sys
input = sys.stdin.readline
import math

n = int(input())
dp = [0]*(n+1)

for i in range(1,n+1):
    m = 1e9
    j = 1
    while j**2 <= i:
        m = min(dp[i-j**2],m)
        j += 1
    dp[i] = m+1
print(dp[n])