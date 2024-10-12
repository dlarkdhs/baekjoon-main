import sys
input = sys.stdin.readline

n,m = map(int,input().split())
for i in range(n,m+1):
    if i == 1:
        continue
    a = 0
    for j in range(2,int(i**(0.5))+1):
        if i % j == 0:
            a = -1
            break
    if a == 0:
        print(i)