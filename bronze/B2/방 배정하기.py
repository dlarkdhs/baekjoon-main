import sys
input = sys.stdin.readline

a,b,c,m = map(int,input().split())

cnt = 0
for i in range(m//a+1):
    for j in range(m//b+1):
        for k in range(m//c+1):
            if a*i+b*j+c*k == m:
                cnt = 1
                break
if cnt == 1:
    print(1)
else:
    print(0)