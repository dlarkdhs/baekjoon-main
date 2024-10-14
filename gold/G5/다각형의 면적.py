import sys
input = sys.stdin.readline

n = int(input())
point = []
for _ in range(n):
    x,y = map(int,input().split())
    point.append((x,y))

N = len(point)
area = 0
for i in range(N):
    x1,y1 = point[i]
    x2,y2 = point[(i+1)%N]
    area += x1*y2 - y1*x2
print(abs(area)/2)