import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int,input().split())))
res = 99999999999
start,end = 0,n-1
one,two = 0,0

while start<end:
    temp = a[start]+a[end]
    zero = abs(temp)
    
    if res>zero:
        res = zero
        one = a[start]
        two = a[end]
    if temp>0:
        end -= 1
    else:
        start += 1
print(one,two)