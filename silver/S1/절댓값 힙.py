import sys
input = sys.stdin.readline
import heapq

n = int(input())

a = []
for _ in range(n):
    t = int(input())
    if t == 0:
        if a:
            print(heapq.heappop(a)[1])
        else:
            print(0)
    else:
        heapq.heappush(a,(abs(t),t))