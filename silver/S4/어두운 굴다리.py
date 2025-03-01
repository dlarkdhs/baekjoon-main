import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
a = list(map(int,input().split()))
res = 0

if m == 1:
    res = max(a[0],n-a[0])
else:
    for i in range(m):
        if i == 0:
            x = a[i]
        elif i == m-1:
            x = n-a[i]
        else:
            d = a[i]-a[i-1]
            if d % 2 == 0:
                x = d//2
            else:
                x = d//2+1
        res = max(x,res)
print(res)