import sys
input = sys.stdin.readline

borad = [[0 for i in range(100)]for i in range(100)]
n = int(input())
for i in range(n):
    x1,y1 = map(int,input().split())
    for j in range(x1,x1+10):
        for k in range(y1,y1+10):
            borad[j][k] = 1
cnt = 0
for row in borad:
    cnt += sum(row)
print(cnt)