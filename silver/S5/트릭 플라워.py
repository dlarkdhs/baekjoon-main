import sys
input = sys.stdin.readline

a,b = map(int,input().split())
r = int(input())
res = [[False]*r for _ in range(r)]
res[a][b] = True

t = 0
while True:
    t += 1
    if a+b+2 < r:
        a += 1
        b += 1
    else:
        a //= 2
        b //= 2
    if res[a][b]:
        print(t)
        break
    res[a][b] = True