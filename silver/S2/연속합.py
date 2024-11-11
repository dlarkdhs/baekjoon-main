import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

s,i = a[0],1
dp = []
dp.append(a[0])
while i < n:
    s += a[i]
    if s < a[i]:
        dp.append(a[i])
        dp.pop()
        s = a[i]
    dp.append(s)
    i += 1
print(max(dp))