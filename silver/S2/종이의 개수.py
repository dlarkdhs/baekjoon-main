import sys
input = sys.stdin.readline

N = int(input())
a = list(list(map(int,input().split())) for _ in range(N))

res = {-1:0,0:0,1:0}
def sol(x,y,n):
    m = a[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if m != a[i][j]:
                sol(x,y,n//3)
                sol(x,y+n//3,n//3)
                sol(x,y+(n//3)*2,n//3)
                sol(x+n//3,y,n//3)
                sol(x+n//3,y+(n//3)*2,n//3)
                sol(x+n//3,y+n//3,n//3)
                sol(x+(n//3)*2,y,n//3)
                sol(x+(n//3)*2,y+(n//3)*2,n//3)
                sol(x+(n//3)*2,y+n//3,n//3)
                return
    res[m] += 1
    return

sol(0,0,N)
for i in res.values():
    print(i)