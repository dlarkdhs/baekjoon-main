import sys
input = sys.stdin.readline

n = int(input())
a = []
dp = []
for i in range(n):
    a.append(float(input()))
    if i == 0:
        dp.append(a[0])
    else:
        dp.append(max(dp[i-1]*a[i],a[i]))
print('%.3f' % max(dp))