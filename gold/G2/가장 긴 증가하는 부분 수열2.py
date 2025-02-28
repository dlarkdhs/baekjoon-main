import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
li = [a[0]]

def sol(x):
    start,end = 0,len(li)-1
    
    while start <= end:
        mid = (start+end)//2
        
        if li[mid] == x:
            return mid
        elif li[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    
    return start

for i in range(n):
    if a[i] > li[-1]:
        li.append(a[i])
    else:
        num = sol(a[i])
        li[num] = a[i]
print(len(li))