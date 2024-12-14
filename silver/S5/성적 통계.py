import sys
input = sys.stdin.readline

k = int(input())

for a in range(k):
    n = list(map(int,input().split()))
    l = n[0]
    n = n[1:]
    n.sort()
    m = n[1]-n[0]
    for i in range(1,l-1):
        if m < n[i+1]-n[i]:
            m = n[i+1]-n[i]
    print(f'Class {a+1}')
    print(f'Max {max(n)}, Min {min(n)}, Largest gap {m}')