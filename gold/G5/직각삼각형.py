import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
t = []

for _ in range(n):
    [x,y] = map(int,input().split())
    t.append([x,y])

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            a = (t[j][0]-t[i][0])**2+(t[j][1]-t[i][1])**2
            b = (t[k][0]-t[j][0])**2+(t[k][1]-t[j][1])**2
            c = (t[k][0]-t[i][0])**2+(t[k][1]-t[i][1])**2
            if a+b==c or b+c==a or a+c==b:
                cnt += 1
print(cnt)