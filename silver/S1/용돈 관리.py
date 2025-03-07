import sys
input = sys.stdin.readline

n,m = map(int,input().split())
money = []
for _ in range(n):
    money.append(int(input()))
    
start,end = max(money),sum(money)

while start <= end:
    mid = (start+end)//2
    presnet = mid
    cnt = 1
    for i in money:
        if presnet - i < 0:
            cnt += 1
            presnet = mid
        presnet -= i
    if cnt > m:
        start = mid + 1
    else:
        end = mid- 1
print(mid)