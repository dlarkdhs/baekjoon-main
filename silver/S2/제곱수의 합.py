import sys
input = sys.stdin.readline

n = int(input())
a = [i for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,i):
        if (j*j) > i:
            break
        if a[i] > a[i-j*j]+1:
            a[i] = a[i-j*j]+1
print(a[n])