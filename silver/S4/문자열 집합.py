import sys
input = sys.stdin.readline

n,m = map(int,input().split())
d = {}
cnt = 0

for i in range(n):
    a = input().rstrip()
    d[a] = True
for i in range(m):
    a = input().rstrip()
    if a in d:
        cnt += 1
print(cnt)