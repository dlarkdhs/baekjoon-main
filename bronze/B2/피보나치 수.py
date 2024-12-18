import sys
input = sys.stdin.readline

n = int(input())

start,end = 0,1
for i in range(n-1):
    start,end = end,start+end
print(end)