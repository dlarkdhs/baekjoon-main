import sys
input = sys.stdin.readline

n,m = map(int,input().split())

find = {}
for _ in range(n):
    a,b = input().split()
    find[a] = b
    
for _ in range(m):
    res = input().rstrip()
    print(find[res])