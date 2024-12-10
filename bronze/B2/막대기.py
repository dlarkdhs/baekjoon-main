import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    stack.append(int(input()))

cnt = 1
m = stack[-1]
for i in range(n-1,-1,-1):
    if m < stack[i]:
        cnt += 1
        m = stack[i]
print(cnt)