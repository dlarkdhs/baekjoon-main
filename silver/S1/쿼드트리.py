import sys
input = sys.stdin.readline

N = int(input())
a = list(list(map(int,input().strip())) for _ in range(N))
res = []

def sol(x,y,n):
    col = a[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if col != a[i][j]:
                print("(",end='')
                sol(x,y,n//2)
                sol(x,y+n//2,n//2)
                sol(x+n//2,y,n//2)
                sol(x+n//2,y+n//2,n//2)
                print(")",end='')
                return
    if col == 0:
        print("0",end='')
    else:
        print("1",end='')
        
sol(0,0,N)