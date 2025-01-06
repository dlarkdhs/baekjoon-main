import sys
input = sys.stdin.readline

n = int(input())


for _ in range(n):
    num = int(input())
    i = 4
    dp = [None,1,2,4]
    while i <= num:
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])
        i += 1
    print(dp[num])