import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a = list(map(int,input().split()))
    if sum(a) % 2 == 0:
        print("YES")
    else:
        print("NO")