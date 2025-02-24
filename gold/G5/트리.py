import sys
input = sys.stdin.readline

def sol(x):
    a[x] = -2
    for i in range(n):
        if x == a[i]:
            sol(i)

n = int(input())
a = list(map(int,input().split()))
start = int(input())

sol(start)
cnt = 0

for i in range(n):
    if a[i] != -2 and i not in a:
        cnt += 1
print(cnt)