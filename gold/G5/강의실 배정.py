import sys
import heapq
input = sys.stdin.readline

n = int(input())

sch = []
for _ in range(n):
    sch.append(list(map(int,input().split())))

sch.sort()
cr = []
heapq.heappush(cr,sch[0][1])
for i in range(1,n):
    if cr[0] <= sch[i][0]:
        heapq.heappop(cr)
    heapq.heappush(cr,sch[i][1])
print(len(cr))