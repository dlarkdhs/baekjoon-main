import sys
input = sys.stdin.readline

n = int(input())
stack = []
ans = []
num = 0
cur = 1
for i in range(n):
    N = int(input())
    while cur <= N:
        stack.append(cur)
        ans.append('+')
        cur += 1
    if stack[-1] == N:
        stack.pop()
        ans.append('-')
    else:
        print("NO")
        num = 1
        break
if num == 0:
    print(*ans, sep='\n')