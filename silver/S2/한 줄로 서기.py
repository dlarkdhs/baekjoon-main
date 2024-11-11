import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))

res = [0]*n
for i in range(1,n+1):
    cnt = 0
    for j in range(n):
        if cnt == a[i-1] and res[j] == 0:
            res[j] = i
            break
        elif res[j] == 0:
            cnt += 1
print(*res)