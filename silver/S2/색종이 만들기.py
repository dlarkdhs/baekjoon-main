import sys
input = sys.stdin.readline

N = int(input())
a = list(list(map(int,input().split())) for _ in range(N))
res = []

def sol(x,y,n):
    col = a[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if col != a[i][j]:
                sol(x,y,n//2)
                sol(x,y+n//2,n//2)
                sol(x+n//2,y,n//2)
                sol(x+n//2,y+n//2,n//2)
                return
    if col == 0:
        res.append(0)
    else:
        res.append(1)
        
sol(0,0,N)
print(res.count(0))
print(res.count(1))