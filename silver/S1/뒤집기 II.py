import sys
input = sys.stdin.readline

n,m = map(int, input().split())

coin = []
for _ in range(n):
    coin.append(list(map(int, input().rstrip())))

ans = 0
def change(x,y):
    for i in range(x+1):
        for j in range(y+1):
            if coin[i][j] == 0:
                coin[i][j] = 1
            else:
                coin[i][j] = 0

for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        if coin[i][j] == 1:
            change(i,j)
            ans += 1
print(ans)