import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]

stk = []
ans = 0

for i in a:
    while stk and stk[-1] <= i:
        stk.pop()
    stk.append(i)
    ans += len(stk)-1
print(ans)