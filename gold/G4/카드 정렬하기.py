import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = sorted([int(input()) for _ in range(n)])
ans = 0

for _ in range(n-1):
    a,b = heapq.heappop(q), heapq.heappop(q)
    c = a+b
    ans += c
    heapq.heappush(q,c)
print(ans)