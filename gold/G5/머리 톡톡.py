import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
li = [0] * 1000001
cnt = [0] * 1000001

for i in a:
    li[i] += 1
    
for i in range(1,1000001):
    if li[i]:
        cnt[i] += li[i]-1
        for j in range(i+i,1000001,i):
            cnt[j] += li[i]

ans = ""
for i in a:
    ans += str(cnt[i])+'\n'
print(ans)