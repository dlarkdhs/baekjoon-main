import sys
input = sys.stdin.readline

a = [[0 for i in range(100)]for i in range(100)]
for i in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(x1,x2):
        for k in range(y1,y2):
            a[j][k] = 1
cnt = 0
for row in a:
    cnt += sum(row)
print(cnt)