import sys
input = sys.stdin.readline

n,k = map(int,input().split())
a = [i for i in range(2,n+1)]

arr = [i for i in range(int(n**0.5)+1)]
arr[0] = 0
arr[1] = 0

for i in range(2,int(len(arr)**(1/2))+1):
    if arr[i] == 0:
        continue
    for j in range(i+i,len(arr),i):
        arr[j] = 0

res = []
for i in arr:
    if arr[i] == 0:
        continue
    for j in a:
        if j % i == 0:
            res.append(j)
            a.remove(j)
result = []
result = res + a
print(result[k-1])