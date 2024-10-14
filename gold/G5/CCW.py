import sys
input = sys.stdin.readline

arr = []
for i in range(3):
    arr.append(list(map(int,input().split())))
x1,y1 = arr[0]
x2,y2 = arr[1]
x3,y3 = arr[2]
res = (x1*y2+x2*y3+x3*y1)-(x2*y1+x3*y2+x1*y3)
if res > 0:
    print(1)
elif res < 0:
    print(-1)
else:
    print(0)