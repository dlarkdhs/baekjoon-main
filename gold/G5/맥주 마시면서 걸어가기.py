import sys
input = sys.stdin.readline
from collections import deque

def sol():
    q = deque()
    q.append([start_x,start_y])
    
    while q:
        x,y = q.popleft()
        if abs(x-end_x)+abs(y-end_y) <= 1000:
            print('happy')
            return
        for i in range(n):
            if not visit[i]:
                nx,ny = p[i]
                if abs(x-nx)+abs(y-ny) <= 1000:
                    visit[i] = 1
                    q.append([nx,ny])
    print('sad')
    return

t = int(input())
for _ in range(t):
    n = int(input())
    p = []
    start_x,start_y = map(int,input().split())
    for i in range(n):
        px,py = map(int,input().split())
        p.append([px,py])
    end_x,end_y = map(int,input().split())
    visit= [0 for _ in range(n+1)]
    sol()