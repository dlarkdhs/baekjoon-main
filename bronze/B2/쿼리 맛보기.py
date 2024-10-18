import sys
input = sys.stdin.readline

n,q = map(int,input().split())
a = list(map(int,input().split()))

for i in range(q):
    sumA = 0
    sumB = 0
    arr = list(map(int,input().split()))
    if arr[0] == 1:
        sumA += sum(a[arr[1]-1:arr[2]])
        print(sumA)
        a[arr[1]-1],a[arr[2]-1] = a[arr[2]-1],a[arr[1]-1]
    elif arr[0] == 2:
        sumA += sum(a[arr[1]-1:arr[2]])
        sumB += sum(a[arr[3]-1:arr[4]])
        print(sumA-sumB)