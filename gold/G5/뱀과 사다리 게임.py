import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
borad = [0]*101
visit = [False]*101

ladder = dict()
snake = dict()

for _ in range(n):
    a,b = map(int,input().split())
    ladder[a] = b
for _ in range(m):
    a,b = map(int,input().split())
    snake[a] = b

q = deque([1])

while q:
    x = q.popleft()
    if x == 100:
        print(borad[x])
        break
    for i in range(1,7):
        y = x+i
        if y <= 100 and not visit[y]:
            if y in ladder.keys():
                y = ladder[y]
            if y in snake.keys():
                y = snake[y]
            if not visit[y]:
                visit[y] = True
                borad[y] = borad[x]+1
                q.append(y)