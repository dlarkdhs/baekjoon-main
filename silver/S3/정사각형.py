import sys
input = sys.stdin.readline

def lenght(p1,p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

n = int(input())
for _ in range(n):
    a = []
    for _ in range(4):
        x,y = map(int,input().split())
        a.append([x,y])
    a.sort()
    p = a[0]
    a[2],a[3] = a[3],a[2]
    d = lenght(p,a[1])
    l = lenght(p,a[2])
    ans = 1
    for i in range(1,4):
        if d != lenght(a[i],a[(i+1)%4]):
            ans = 0
    if l != lenght(a[1],a[3]):
        ans = 0
    print(ans)