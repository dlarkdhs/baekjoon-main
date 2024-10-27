import sys
input = sys.stdin.readline

a,b = map(int,input().split())
arr = [i for i in range(int(b**(1/2))+1)]
arr[0] = 0
arr[1] = 0
cnt = 0

for i in range(2,int(len(arr)**(1/2))+1):
    if arr[i] == 0:
        continue
    for j in range(i+i,len(arr),i):
        arr[j] = 0

for i in arr:
    if arr[i] == 0:
        continue
    num = i
    while num <= b:
        num *= i
        if a <= num <= b:
            cnt += 1
print(cnt)