import sys
input = sys.stdin.readline

a = list(True for _ in range(1000001))
a[0] = a[1] = False
for i in range(2,1000001):
    if a[i]:
        for j in range(i*2,1000001,i):
            a[j] = False
t = int(input())
for _ in range(t):
    n = int(input())
    count = 0
    for i in range(2,n//2+1):
        if a[i] and a[n-i]:
            count += 1
    print(count)