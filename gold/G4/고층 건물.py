import sys
input = sys.stdin.readline

def line(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)

n = int(input())
a = list(map(int,input().split()))

res = 0
for i1,y1 in enumerate(a):
    x1 = i1+1
    
    current_r = None
    vr = 0
    for i2 in range(i1+1,n+1):
        if i2 == n:
            break
        x2 = i2+1
        y2 = a[i2]
        l = line(x1,y1,x2,y2)
        if current_r == None or current_r < l:
            current_r = l
            vr += 1
    
    current_l = None
    vl = 0
    for i3 in range(i1-1,-1,-1):
        if i3 == -1:
            break
        x3 = i3+1
        y3 = a[i3]
        l = line(x1,y1,x3,y3)
        if current_l == None or current_l > l:
            current_l = l
            vl += 1
        
    if res < vl+vr:
        res = vl+vr
print(res)