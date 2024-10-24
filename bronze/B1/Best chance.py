import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a1 = list(map(int, input().split()))

max1 = max(a)
max1_index = a.index(max1)

max2 = max([a[i] for i in range(n) if i != max1_index])

res = []

for i in range(n):
    if i == max1_index:
        max_a = max2
    else:
        max_a = max1
    
    res.append(max_a - a1[i])

for i in range(n):
    print((res[i] - (a[i] - a1[i]))*-1, end=' ')
